<!-- src/Sidebar.svelte -->
<script>
  export const active = 'detail_payment';
  import Sidebar from '../sidebar/+page.svelte';
</script>

<style>
  .detail_payment {
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

<div class="detail_payment">
  <Sidebar active="detail_payment" />
  <div class="content">
    <h1>Welcome to the Detail Payment</h1>
    <!-- Add more content here -->
  </div>
</div>
