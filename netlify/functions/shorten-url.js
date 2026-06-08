exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return jsonResponse(405, { error: 'Method not allowed' });
  }

  const token = process.env.TINYURL_API_TOKEN || process.env.TINYURL_TOKEN;
  if (!token) {
    return jsonResponse(500, { error: 'TinyURL API token is not configured' });
  }

  let body;
  try {
    body = JSON.parse(event.body || '{}');
  } catch (error) {
    return jsonResponse(400, { error: 'Invalid JSON body' });
  }

  const url = typeof body.url === 'string' ? body.url.trim() : '';
  if (!url) {
    return jsonResponse(400, { error: 'URL is required' });
  }

  let parsedUrl;
  try {
    parsedUrl = new URL(url);
  } catch (error) {
    return jsonResponse(400, { error: 'Invalid URL' });
  }

  if (!['http:', 'https:'].includes(parsedUrl.protocol)) {
    return jsonResponse(400, { error: 'URL must use HTTP or HTTPS' });
  }

  try {
    const tinyUrlResponse = await fetch('https://api.tinyurl.com/create', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        url,
        domain: process.env.TINYURL_DOMAIN || 'tinyurl.com',
      }),
    });

    const result = await tinyUrlResponse.json().catch(() => ({}));

    if (!tinyUrlResponse.ok) {
      return jsonResponse(tinyUrlResponse.status, {
        error:
          result?.errors?.[0] ||
          result?.message ||
          result?.error ||
          'TinyURL request failed',
      });
    }

    const shortUrl = result?.data?.tiny_url;
    if (!shortUrl) {
      return jsonResponse(502, { error: 'TinyURL response did not include a short URL' });
    }

    return jsonResponse(200, { shortUrl });
  } catch (error) {
    return jsonResponse(502, { error: 'Unable to reach TinyURL API' });
  }
};

function jsonResponse(statusCode, body) {
  return {
    statusCode,
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  };
}
