document.querySelector('.login-form').addEventListener('submit', function (e) {
  e.preventDefault();
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  if (email && password) {
    alert(Bem-vindo, ${email});
  } else {
    alert('Por favor, preencha todos os campos!');
  }
});
