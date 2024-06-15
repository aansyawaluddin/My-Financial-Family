<script>
  // @ts-nocheck // Mengabaikan pengecekan tipe TypeScript untuk file ini
  
  import { goto } from '$app/navigation'; // Mengimpor fungsi goto dari modul navigasi Svelte
  import { onMount } from 'svelte'; // Mengimpor fungsi onMount dari modul Svelte untuk menangani siklus hidup komponen
  import { userStore } from '../store'; // Mengimpor store user dari lokasi yang sesuai
  
  export let active = 'sidebar'; // Properti untuk menentukan menu aktif secara dinamis
  
  let user = {}; // Objek untuk menyimpan data pengguna yang diperoleh dari store
  
  // Subscribe to the store to get user data
  userStore.subscribe(value => {
    user = value || {}; // Mengupdate nilai objek user saat ada perubahan di store
  });
  
  // Menangani peristiwa saat komponen dimuat pertama kali
  onMount(() => {
    const isLoggedIn = localStorage.getItem('isLoggedIn'); // Mendapatkan status login dari localStorage
    if (!isLoggedIn) {
      goto('login'); // Jika tidak ada status login, arahkan pengguna ke halaman login
    }
  
    // Event listener untuk menangani peristiwa saat tombol back ditekan
    const handlePopState = () => {
      logout(); // Panggil fungsi logout saat tombol back ditekan
    };
  
    window.addEventListener('popstate', handlePopState); // Tambahkan event listener untuk tombol back
  
    // Membersihkan event listener saat komponen dihancurkan atau tidak lagi digunakan
    return () => {
      window.removeEventListener('popstate', handlePopState); // Hapus event listener saat komponen di-unmount
    };
  });
  
  // Fungsi untuk logout pengguna
  function logout() {
    localStorage.removeItem('isLoggedIn'); // Hapus status login dari localStorage
    goto('login'); // Redirect pengguna ke halaman login setelah logout
  }
  
  // Event listener untuk menangani perubahan URL
  const handleUrlChange = () => {
    // Periksa apakah referrer tidak dimulai dengan origin yang sama dengan window location
    if (!document.referrer.startsWith(window.location.origin)) {
      logout(); // Jika tidak, panggil fungsi logout untuk memastikan logout saat pengguna meninggalkan halaman
    }
  };
  
  window.addEventListener('beforeunload', handleUrlChange); // Tambahkan event listener untuk perubahan URL
  
  </script>
  
  
  <style>
  .sidebar {
    width: 150px;
    height: 92.3vh;
    background-color: #111827;
    color: white;
    padding: 1.5rem;
  }
  .logo {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 1rem;
    color: #3B82F6;
  }
  .menu {
    margin-top: 2rem;
    flex: 1;
  }
  .menu a {
    display: block;
    padding: 0.75rem 1rem;
    color: white;
    text-decoration: none;
    border-radius: 0.5rem;
    margin-bottom: 0.5rem;
  }
  .menu a.active,
  .menu a:hover {
    background-color: #2563eb; /* Warna yang sama untuk menu aktif dan menu dihover */
  }
  .profile {
    display: flex;
    align-items: center;
    padding: 1rem;
    background-color: #1F2937;
    border-radius: 0.5rem;
    margin-top: auto;
  }
  .profile img {
    border-radius: 50%;
    width: 40px;
    height: 40px;
    margin-right: 1rem;
  }
  .logout {
    display: block;
    padding: 0.75rem 1rem;
    margin-top: 1rem;
    background-color: #6B7280;
    color: white;
    text-decoration: none;
    text-align: center;
    border-radius: 0.5rem;
  }
  </style>
  
  <div class="sidebar">
    <div class="logo">My Financial Family</div>
    <div class="menu">
      <a href="home" class="{active === 'home' ? 'active' : ''}">Home</a>
      <a href="expenses" class="{active === 'expenses' ? 'active' : ''}">Expenses</a>
      <a href="transaction" class="{active === 'transaction' ? 'active' : ''}">Transactions</a>
      <a href="detail-payment" class="{active === 'detail-payment' ? 'active' : ''}">Detail Payment</a>
      <a href="family" class="{active === 'family' ? 'active' : ''}">Family</a>
    </div>
    <div class="profile">
      <img src="https://i.pinimg.com/474x/a3/f4/bc/a3f4bc0dc7d1b030b782c62d7a4781cf.jpg" alt="Profile Picture" />
      <div>
        <div>{user.Fullname}</div>
        <a href="profile-user">View profile</a>
      </div>
    </div>
    <button on:click={logout} class="logout">Logout</button>
  </div>
  