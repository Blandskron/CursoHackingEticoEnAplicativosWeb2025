document.getElementById('loginForm').addEventListener('submit', async function (e) {
  e.preventDefault();
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  await fetch('http://localhost:8001/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
});

async function submitComment() {
  const comment = document.getElementById('commentInput').value;

  await fetch('http://localhost:8001/comment', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ comment })
  });

  const response = await fetch('http://localhost:8001/comments');
  const comments = await response.json();

  const commentContainer = document.getElementById('comments');
  commentContainer.innerHTML = comments.map(c => `<p>${c}</p>`).join('');
}
