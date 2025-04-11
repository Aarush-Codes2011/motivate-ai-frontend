document.getElementById('form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const form = e.target;
  const formData = new FormData(form);

  const response = await fetch('https://your-backend-url.onrender.com/generate', {
    method: 'POST',
    body: formData
  });

  const result = await response.json();
  alert("Generated Successfully: " + result.message);
});
