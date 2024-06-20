<!-- src/Sidebar.svelte -->
<script>
  export const active = 'payment-method';
  import Sidebar from '../sidebar/+page.svelte';
</script>

<style>
  .payment-method {
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

<div class="payment-method">
  <Sidebar active="payment-method" />
  <div class="content">
    <h1>Welcome to the Payment Method</h1>
    <!-- Add more content here -->
  </div>
</div>
