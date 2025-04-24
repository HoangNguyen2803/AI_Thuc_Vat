document.getElementById('iris-form').addEventListener('submit', async function(e) {
  e.preventDefault();
  const form = e.target;
  const data = {
    sepal_length: form.sepal_length.value,
    sepal_width: form.sepal_width.value,
    petal_length: form.petal_length.value,
    petal_width: form.petal_width.value
  };

  const res = await fetch('/predict', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  });

  const json = await res.json();
  document.getElementById('result').textContent = json.result || json.error;
});
