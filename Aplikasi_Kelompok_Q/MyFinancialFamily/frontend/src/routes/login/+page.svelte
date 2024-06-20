<script>
  // @ts-nocheck // Mengabaikan pengecekan tipe TypeScript untuk file ini

  import { goto } from '$app/navigation'; // Mengimpor fungsi goto dari modul navigasi Svelte
  import { userStore } from '../store'; // Mengimpor store user dari lokasi yang sesuai

  let email = ""; // Variabel untuk menyimpan nilai input email dari pengguna
  let password = ""; // Variabel untuk menyimpan nilai input password dari pengguna
  let rememberMe = false; // Variabel boolean untuk mengontrol opsi "Keep me signed in"
  // let user = {}; // Variabel untuk menyimpan data pengguna setelah login


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
    margin: 70px auto;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
</style>

<div class="container login-container">
  <div class="text-center mb-4">
    <h1 class="h3 mb-3 font-weight-normal">My Financial Family</h1>
  </div>
  <div class="form-group">
    <label for="email" class="form-label">Email Address</label>
    <input type="text" id="email" bind:value={email} class="form-control" />
  </div>
  <div class="form-group">
    <label for="password" class="form-label">Password</label>
    <a href="#" class="float-right">Forgot Password?</a>
    <input type="password" id="password" bind:value={password} class="form-control" />
  </div>
  <div class="form-group form-check">
    <input type="checkbox" id="rememberMe" bind:checked={rememberMe} class="form-check-input" />
    <label for="rememberMe" class="form-check-label">Keep me signed in</label>
  </div>
  <button class="btn btn-primary w-100" on:click={handleLogin}>Login</button>
  <div class="text-center mt-3">
    <a href="signup" class="text-primary">Create an account</a>
  </div>
</div>
