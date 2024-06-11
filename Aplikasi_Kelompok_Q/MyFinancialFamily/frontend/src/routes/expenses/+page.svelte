<!-- src/Sidebar.svelte -->
<script>
  export const active = 'expenses';
  import Sidebar from '../sidebar/+page.svelte';
</script>

<style>
  .expenses {
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

<div class="expenses">
  <Sidebar active="expenses" />
  <div class="content">
    <h1>Welcome to the Expenses</h1>
    <!-- Add more content here -->
  </div>
</div>
