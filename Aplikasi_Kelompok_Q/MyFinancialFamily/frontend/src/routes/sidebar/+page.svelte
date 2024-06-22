<script>
  export let active = 'sidebar';
</script>

<style>
  .sidebar {
    height: auto;
  }
  .logo {
    color: #3B82F6;
  }
  .profile img {
    border-radius: 50%;
    width: 40px;
    height: 40px;
    margin-right: 1rem;
  }
</style>

<div class="d-flex flex-column bg-dark text-white p-3 sidebar">
  <div class="logo h3 mb-4">My Family Finances</div>
  <div class="menu flex-grow-1">
    <a href="home" class="nav-link text-white py-2 px-3 mb-2 {active === 'home' ? 'bg-primary' : 'bg-dark'}">Home</a>
    <a href="expenses" class="nav-link text-white py-2 px-3 mb-2 {active === 'expenses' ? 'bg-primary' : 'bg-dark'}">Expenses</a>
    <a href="transaction" class="nav-link text-white py-2 px-3 mb-2 {active === 'transaction' ? 'bg-primary' : 'bg-dark'}">Transactions</a>
    <a href="detail_payment" class="nav-link text-white py-2 px-3 mb-2 {active === 'detail_payment' ? 'bg-primary' : 'bg-dark'}">Detail Payment</a>
    <a href="family" class="nav-link text-white py-2 px-3 mb-2 {active === 'family' ? 'bg-primary' : 'bg-dark'}">Family</a>
  </div>
  <div class="profile d-flex align-items-center p-3 bg-secondary rounded mt-auto">
    <img src="" alt="Profile Picture" />
    <div>
      <div>Andi muh Haikal</div>
      <a href="#" class="text-white">View profile</a>
    </div>
  </div>
  <a href="/" class="btn btn-secondary mt-3 text-white text-center">Logout</a>
</div>
