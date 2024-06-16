<!-- src/Sidebar.svelte -->
<script>
  // Impor fungsi 'goto' dari '$app/navigation' untuk navigasi
  import { goto } from '$app/navigation';
  
  // Impor userStore dari store yang digunakan untuk menyimpan data pengguna
  import { userStore } from '../store';

  // Deklarasi variabel untuk menyimpan data yang diinputkan pengguna pada form pendaftaran
  let username = "";
  let fullname = "";
  let email = "";
  let password = "";
  let gender = ""; // Variabel untuk menyimpan jenis kelamin pengguna
  let role = ""; // Variabel untuk menyimpan peran pengguna
  let familyemail = ""; 
  let rememberMe = false; // Variabel untuk menyimpan pilihan "ingat saya" pengguna

  // Fungsi yang akan dipanggil ketika pengguna mengklik tombol "Sign up"
  async function handleSignup() {
    // Membuat objek user yang berisi data yang diinputkan pengguna
    const user = {
      Username: username,
      Fullname: fullname,
      Password: password,
      Gender: gender,
      Email: email.toLowerCase(), // Konversi email ke huruf kecil
      Role: role,
      FamilyEmail: familyemail
    };

    // Validasi input, memastikan semua bidang telah diisi
    if (!username || !fullname || !email || !password || !gender || !role || !familyemail) {
      alert("Please fill in all fields");
      return;
    }

    // Validasi panjang username tidak boleh lebih dari 10 karakter
    if (username.length > 10) {
      alert("Nickname cannot exceed 10 characters");
      return;
    }

    try {
      // Mengirimkan permintaan POST ke server untuk membuat pengguna baru
      const response = await fetch('http://127.0.0.1:8000/users/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
      });

      // Jika respons dari server sukses (status 200), simpan data pengguna di userStore dan navigasi ke halaman 'home'
      if (response.ok) {
        const result = await response.json();
        userStore.set(result.user); // Simpan objek user ke userStore
        localStorage.setItem('isLoggedIn', 'true');
        goto('home'); // Navigasi ke halaman 'home'
      } else {
        // Jika email sudah digunakan, tampilkan pesan kesalahan
        alert("Email is already taken");
      }
    } catch (error) {
      // Jika terjadi kesalahan saat mengirim permintaan ke server, tampilkan di konsol
      console.error("Error:", error);
    }
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
  .form-group input[type="password"],
  .form-group select { /* Menambahkan gaya untuk select */
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: 'Inter', sans-serif;
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
    <label for="name">Username</label>
    <input type="text" id="username" bind:value={username} maxlength="10"  placeholder="Enter Username (max 10)"/>
  </div>
  <div class="form-group">
    <label for="fullname">Fullname</label>
    <input type="text" id="fullname" bind:value={fullname}  placeholder="Enter Full Name"/>
  </div>
  <div class="form-group">
    <label for="email">Email Address</label>
    <input type="email" id="email" bind:value={email} placeholder="Enter Email"/>
  </div>
  <div class="form-group">
    <label for="password">Password</label>
    <input type="password" id="password" bind:value={password} placeholder="Enter Password"/>
  </div>
  <div class="form-group">
    <label for="gender">Gender</label>
    <select id="gender" bind:value={gender}>
      <option value="">Select Gender</option>
      <option value="male">Male</option>
      <option value="female">Female</option>
    </select>
  </div>
  <div class="form-group">
    <label for="familyemail">Family Email</label>
    <input type="text" id="familyemail" bind:value={familyemail} placeholder="Enter Family Email" />
  </div>
  <div class="form-group">
    <label for="role">Role</label>
    <input type="text" id="role" bind:value={role} placeholder="Enter Role" />
  </div>

  <button class="btn-signup" on:click={handleSignup}>Sign up</button>
  <div class="already-account">
    <span>Already have an account? </span><a href="/login">Sign in here</a>
  </div>
</div>
