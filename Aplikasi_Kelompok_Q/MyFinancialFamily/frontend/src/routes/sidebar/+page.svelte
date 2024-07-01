<script>
  // @ts-nocheck // Mengabaikan pengecekan tipe TypeScript untuk file ini
  
  import { goto } from '$app/navigation'; // Mengimpor fungsi goto dari modul navigasi Svelte
  import { onMount } from 'svelte'; // Mengimpor fungsi onMount dari modul Svelte untuk menangani siklus hidup komponen
  import { userStore } from '../store'; // Mengimpor store user dari lokasi yang sesuai
  
  export let active = 'sidebar'; // Properti untuk menentukan menu aktif secara dinamis
  
  let user = {}; // Objek untuk menyimpan data pengguna yang diperoleh dari store
  
  // Menangani peristiwa saat komponen dimuat pertama kali
  onMount(() => {
    const isLoggedIn = sessionStorage.getItem('isLoggedIn'); // Mendapatkan status login dari sessionStorage
    if (!isLoggedIn) {
      goto('login'); // Jika tidak ada status login, arahkan pengguna ke halaman login
    } else {
      getDataUser(); // Panggil fungsi untuk mengambil data pengguna dari backend setelah login berhasil
    }
    
  });

  async function getDataUser() {
    try {
      const getUsername = sessionStorage.getItem('Username');
      const response = await fetch(`http://127.0.0.1:8000/users/read-username/${getUsername}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        const result = await response.json();
        user = result.user;
        userStore.set(result.user); // Disesuaikan dengan struktur respons dari server
      } else {
        console.error("Failed to fetch user data:", response.status, response.statusText);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  // Fungsi untuk logout pengguna
  function logout() {
    sessionStorage.removeItem('isLoggedIn'); // Hapus status login dari sessionStorage
    sessionStorage.removeItem('user'); // Hapus status login dari sessionStorage
    sessionStorage.removeItem('Username'); // Hapus status login dari sessionStorage
    goto('login'); // Redirect pengguna ke halaman login setelah logout
  }
</script>

<style>
  .sidebar {
    display: flex;
    width: 288px;
    height: 1059px;
    padding: 48px 28px;
    flex-direction: column;
    justify-content: space-between;

    flex-shrink: 0;
  }
  .home a:hover {
    background-color: #0B63F8;
  }
  .menu a {
    transition: background-color 0.3s ease;
  }
  .menu a:hover {
    background-color: #0B63F8; 
  }
  .profile {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 16px;
    margin-top: auto;
    margin-bottom: auto;
  }
  .profile:hover {
    background-color: #0B63F8;
    color: white;
  }
.btn {
  background-color: #444444;
  color: white;
}

.text-decoration-none {
  color: #BABABA;
}
.text-decoration-none:hover {
  color: white;
}
.logo {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 1rem;
    background: linear-gradient(90deg, #406DD4 40%, #474343 90%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

</style>



<div class="sidebar bg-dark text-white p-3 position-fixed vh-100">
  <div class="logo fs-4 fw-bold text-primary mb-3">My Financial Family</div>
  <div class="menu flex-grow-1">
    <a href="home" class="d-block p-2 mb-1 text-decoration-none rounded {active === 'home' ? 'bg-primary text-white' : ''}">
      <i class="bi bi-house-door me-2"></i>Home
    </a>
    <a href="expenses" class="d-block p-2 mb-1 text-decoration-none rounded {active === 'expenses' ? 'bg-primary text-white' : ''}">
      <i class="bi bi-cash-stack me-2"></i>Expenses
    </a>
    <a href="payment-method" class="d-block p-2 mb-1 text-decoration-none rounded {active === 'payment-method' ? 'bg-primary text-white' : ''}">
      <i class="bi bi-credit-card me-2"></i>Payment Method
    </a>
    <a href="transaction" class="d-block p-2 mb-1 text-decoration-none rounded {active === 'transaction' ? 'bg-primary text-white' : ''}">
      <i class="bi bi-arrow-left-right me-2"></i>Transactions
    </a>
    <a href="detail-payment" class="d-block p-2 mb-1 text-decoration-none rounded {active === 'detail-payment' ? 'bg-primary text-white' : ''}">
      <i class="bi bi-info-circle me-2"></i>Detail Payment
    </a>
    <a href="family" class="d-block p-2 mb-1 text-decoration-none rounded {active === 'family' ? 'bg-primary text-white' : ''}">
      <i class="bi bi-people me-2"></i>Family
    </a>
  </div>
  <div class="profile d-flex align-items-center p-3 rounded mt-3">
    <img src={"https://i.pinimg.com/474x/a3/f4/bc/a3f4bc0dc7d1b030b782c62d7a4781cf.jpg"} alt="Profile Picture" class="rounded-circle me-3" style="width: 40px; height: 40px;" />
    <div>
      <div>{user.Username}</div>
      <a href="profile-user" class="text-decoration-none ">View profile</a>
    </div>
  </div>
  <button on:click={logout} class="btn w-100 mt-3">Logout</button>
</div>
