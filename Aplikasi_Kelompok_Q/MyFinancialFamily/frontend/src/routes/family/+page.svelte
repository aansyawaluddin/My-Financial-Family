<script>
// @ts-nocheck

  export const active = 'family';
  import Sidebar from '../sidebar/+page.svelte';
  import { userStore } from '../store';
  let familyMembers = [];
  let user = {};
  
  userStore.subscribe(value => {
    user = value || {};
    readAllUser();
  });

  async function readAllUser() {
    try {
      const response = await fetch(`http://127.0.0.1:8000/users/read-all-users?family_email=${user.FamilyEmail}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        const result = await response.json();
        familyMembers = result.users;
      } else {
        alert("Failed to fetch family members");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }
</script>

<style>
  .layout {
      display: flex;
  }
  .sidebar {
      width: 250px;
      flex-shrink: 0;
  }
  .content {
      flex-grow: 1;
      padding: 20px;
      margin-left: 90px;
  }
  .family-members {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
  }
  .card {
      width: 200px;
      height: 180px;
      box-sizing: border-box;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 10px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
  }
  .card img {
      border-radius: 50%;
      width: 100px;
      height: 100px;
  }
  .card .name {
      font-weight: bold;
      margin-top: 10px;
  }
  .card .role {
      color: gray;
  }
</style>

<div class="layout">
  <div class="sidebar">
      <Sidebar active="family" />
  </div>
  <div class="content">
      <h1>Hello, {user.Fullname}</h1>
      <h2>Family Members</h2>
      <div class="family-members">
          {#each familyMembers as member}
              <div class="card">
                  <img src="https://i.pinimg.com/474x/a3/f4/bc/a3f4bc0dc7d1b030b782c62d7a4781cf.jpg" alt={member.Fullname} />
                  <div class="name">{member.Fullname}</div>
                  <div class="role">{member.Role}</div>
              </div>
          {/each}
      </div>
  </div>
</div>
