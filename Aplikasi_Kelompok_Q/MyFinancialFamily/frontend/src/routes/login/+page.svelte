<script>
  // @ts-nocheck // Mengabaikan pengecekan tipe TypeScript untuk file ini
  
  import { goto } from '$app/navigation'; // Mengimpor fungsi goto dari modul navigasi Svelte
  import { userStore } from '../store'; // Mengimpor store user dari lokasi yang sesuai
  
  let email = ""; // Variabel untuk menyimpan nilai input email dari pengguna
  let password = ""; // Variabel untuk menyimpan nilai input password dari pengguna
  let rememberMe = false; // Variabel boolean untuk mengontrol opsi "Keep me signed in"
  // let user = {}; // Variabel untuk menyimpan data pengguna setelah login
  let getUserID = {};
  
  /**
   * Fungsi handleLogin digunakan untuk menangani proses login pengguna
   * Mengirimkan permintaan POST ke endpoint '/login/' dengan kredensial pengguna
   */
  async function handleLogin() {
    const credentials = {
      Email: email,
      Password: password
    };
  
    try {
      const response = await fetch('http://127.0.0.1:8000/login/', {
        method: 'POST', // Metode permintaan POST
        headers: {
          'Content-Type': 'application/json' // Header untuk konten JSON
        },
        body: JSON.stringify(credentials) // Mengubah objek credentials menjadi string JSON
      });
  
      if (response.ok) { // Jika permintaan berhasil (kode status 200-299)
        const result = await response.json(); // Mendapatkan data JSON dari respons
  
        console.log("Login successful", result); // Pesan log untuk berhasil login
        // getUserID = result.user;
        sessionStorage.setItem('isLoggedIn', 'true'); // Menyimpan status login di sessionStorage
        sessionStorage.setItem('UserID', result.user.UserID); // Menyimpan status login di sessionStorage
  
        // Menyimpan data pengguna ke store (misalnya userStore)
        // userStore.set(result.user); // Disesuaikan dengan struktur respons dari server
  
        goto('home'); // Mengarahkan pengguna ke halaman 'home' setelah login berhasil
      } else if (response.status === 400) { // Jika kesalahan kredensial (kode status 400)
        alert("Incorrect password"); // Menampilkan pesan kesalahan: password salah
      } else if (response.status === 404) { // Jika email tidak ditemukan (kode status 404)
        alert("Email not found"); // Menampilkan pesan kesalahan: email tidak ditemukan
      } else { // Jika respons lain dengan kode status yang tidak diharapkan
        console.error("Login failed", response.statusText); // Pesan log untuk kegagalan login
      }
    } catch (error) {
      console.error("Error:", error); // Menangkap dan menampilkan kesalahan jika terjadi
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