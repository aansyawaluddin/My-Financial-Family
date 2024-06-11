<!-- src/Sidebar.svelte -->
<script>
  export const active = 'transaction';
  import Sidebar from '../sidebar/+page.svelte';
</script>

<style>
  .transaction {
    display: flex;
    height: 100vh;
    box-sizing: border-box;
  }
  .content {
    flex: 1;
    padding: 1rem;
    overflow-y: auto;
  }
</style>

<div class="transaction">
  <Sidebar active="transaction" />
  <div class="content">
    <h1>Welcome to the Transactions</h1>
    <!-- Add more content here -->
  </div>
</div>
