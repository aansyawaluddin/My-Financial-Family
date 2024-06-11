<!-- src/Sidebar.svelte -->
<script>
  export const active = 'family';
  import Sidebar from '../sidebar/+page.svelte';
</script>

<style>
  .family {
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

<div class="family">
  <Sidebar active="family" />
  <div class="content">
    <h1>Welcome to the Family</h1>
    <!-- Add more content here -->
  </div>
</div>
