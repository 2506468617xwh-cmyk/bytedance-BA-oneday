export async function onRequestPost(context) {
  const DEEPSEEK_KEY = context.env.DEEPSEEK_API_KEY;
  const body = await context.request.text();

  const resp = await fetch('https://api.deepseek.com/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + DEEPSEEK_KEY,
    },
    body,
  });

  const data = await resp.text();
  return new Response(data, {
    headers: { 'Content-Type': 'application/json' },
  });
}
