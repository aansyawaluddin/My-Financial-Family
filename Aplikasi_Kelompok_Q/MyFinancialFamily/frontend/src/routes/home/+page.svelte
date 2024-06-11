<!-- src/Sidebar.svelte -->
<script>
  export const active = 'home';
  import Sidebar from '../sidebar/+page.svelte';
</script>

<style>
  .home {
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

<div class="home">
  <Sidebar active="home" />
  <div class="content">
    <h1>Welcome to the Dashboard</h1>
    <!-- Add more content here -->
  </div>
</div>
