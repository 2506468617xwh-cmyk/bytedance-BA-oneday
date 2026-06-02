export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // 1. 如果前端请求的是大模型 AI 接口，直接进行代理转发
    if (url.pathname === '/api/chat' && request.method === 'POST') {
      try {
        const body = await request.json();
        const response = await fetch('https://api.deepseek.com/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${env.deepseekapi}` // 依然使用你的小写环境变量
          },
          body: JSON.stringify(body)
        });
        const data = await response.json();
        return new Response(JSON.stringify(data), {
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          }
        });
      } catch (error) {
        return new Response(JSON.stringify({ error: error.message }), {
          status: 500,
          headers: { 'Content-Type': 'application/json' }
        });
      }
    }

    // 2. 如果是其他请求（如主页、图片素材等），无缝交回给 Cloudflare 默认的静态资源托管
    return env.ASSETS.fetch(request);
  }
};
