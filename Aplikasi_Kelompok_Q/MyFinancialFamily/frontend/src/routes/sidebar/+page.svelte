<!-- src/Sidebar.svelte -->
<script>
  export let active = 'sidebar';
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
    <a href="detail_payment" class="{active === 'detail_payment' ? 'active' : ''}">Detail Payment</a>
    <a href="family" class="{active === 'family' ? 'active' : ''}">Family</a>
  </div>
  <div class="profile">
    <img src="path/to/profile.jpg" alt="Profile Picture" />
    <div>
      <div>Andi muh Haikal</div>
      <a href="#">View profile</a>
    </div>
  </div>
  <a href="/" class="logout">Logout</a>
</div>
