<script>
  let name = "";
  let email = "";
  let password = "";
  let rememberMe = false;

  function handleSignup() {
    console.log("Name:", name);
    console.log("Email:", email);
    console.log("Password:", password);
    console.log("Remember Me:", rememberMe);
    
  }
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

  .signup-container {
    font-family: 'Inter', sans-serif;
    max-width: 400px;
    align-self: center;
	  margin: 70px 0px 0px 250px;
    padding: 4rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  .signup-header {
    text-align: center;
    font-size: 1.5rem;
    margin-bottom: 1rem;
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
  .form-group input[type="email"],
  .form-group input[type="password"] {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: 'Inter', sans-serif;
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
  .btn-signup {
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
  .btn-signup:hover {
    background-color: #2563EB;
  }
  .already-account {
    text-align: center;
    margin-top: 1rem;
    font-size: 0.875rem;
  }
  .already-account a {
    color: #3B82F6;
    text-decoration: none;
  }
  .already-account a:hover {
    text-decoration: underline;
  }
</style>

<div class="signup-container">
  <div class="signup-header">My Financial Family</div>
  <div class="form-group">
    <label for="name">Name</label>
    <input type="text" id="name" bind:value={name} />
  </div>
  <div class="form-group">
    <label for="email">Email Address</label>
    <input type="email" id="email" bind:value={email} />
  </div>
  <div class="form-group">
    <label for="password">Password</label>
    <input type="password" id="password" bind:value={password} />
  </div>
 
  <button class="btn-signup" on:click={handleSignup}>Sign up</button>
  <div class="already-account">
    <span>Already have an account? </span><a href="/">Sign in here</a> <!-- Menambahkan link ke halaman login -->
  </div>
</div>