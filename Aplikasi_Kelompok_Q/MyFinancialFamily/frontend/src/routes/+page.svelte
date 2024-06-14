<script>
 import { goto } from '$app/navigation';

  let email = "";
  let password = "";
  let rememberMe = false;

  async function handleLogin() {
    const credentials = {
      Email: email,
      Password: password
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
      });

      if (response.ok) {
        const result = await response.json();
        console.log("Login successful", result);
        goto('home');
      } else if (response.status === 400) {
        alert("Incorrect password");
      } else if (response.status === 404) {
        alert("Email not found");
      } else {
        console.error("Login failed", response.statusText);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

  .login-container {
    font-family: 'Inter', sans-serif;
    max-width: 400px;
    padding: 2rem;
	align-self: center;
	margin: 70px 0px 0px 250px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  .login-header {
    text-align: center;
    font-size: 1.5rem;
    margin-bottom: 3rem;
    font-weight: 600;
    color: #3B82F6;
  }
  .form-group {
    margin-bottom: 1rem;
  }
  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 600;
  }
  .form-group input[type="text"],
  .form-group input[type="password"] {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: 'Inter', sans-serif;
  }
  .form-group .forgot-password {
    float: right;
    font-size: 0.875rem;
    color: #3B82F6;
    cursor: pointer;
    text-decoration: none;
  }
  .form-group .forgot-password:hover {
    text-decoration: underline;
  }
  .form-group .remember-me {
    display: flex;
    align-items: center;
  }
  .form-group .remember-me input {
    margin-right: 0.5rem;
  }
  .form-group .remember-me label {
    margin: 0;
    font-weight: 400;
  }
  .btn-login {
    width: 100%;
    padding: 0.75rem;
    background-color: #3B82F6;
    border: none;
    border-radius: 4px;
    color: #fff;
    font-size: 1rem;
    cursor: pointer;
    font-weight: 600;
  }
  .btn-login:hover {
    background-color: #2563EB;
  }
  .create-account {
    text-align: center;
    margin-top: 1rem;
    font-size: 0.875rem;
  }
  .create-account a {
    color: #3B82F6;
    text-decoration: none;
  }
  .create-account a:hover {
    text-decoration: underline;
  }
</style>

<div class="login-container">
  <div class="login-header">My Financial Family</div>
  <div class="form-group">
    <label for="email">Email Address</label>
    <input type="text" id="email" bind:value={email} />
  </div>
  <div class="form-group">
    <label for="password">Password</label>
    <a href="#" class="forgot-password">Forgot Password?</a>
    <input type="password" id="password" bind:value={password} />
  </div>
  <div class="form-group remember-me">
    <input type="checkbox" id="rememberMe" bind:checked={rememberMe} />
    <label for="rememberMe">Keep me signed in</label>
  </div>
  <button class="btn-login" on:click={handleLogin}>Login</button>
<div class="create-account">
  <a href="signup">Create an account</a>
</div>

</div>