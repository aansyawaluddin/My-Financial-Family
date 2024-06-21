<!-- src/Sidebar.svelte -->
<script>
// @ts-nocheck

  export const active = 'home';
  import Sidebar from '../sidebar/+page.svelte';
  import { userStore } from '../store';


  let user = {};

  // Subscribe to the store to get user data
  userStore.subscribe(value => {
    user = value 
});
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
    <h1>Welcome to the Dashboard {user.Fullname}</h1>
    <!-- Add more content here -->
  </div>
</div>
