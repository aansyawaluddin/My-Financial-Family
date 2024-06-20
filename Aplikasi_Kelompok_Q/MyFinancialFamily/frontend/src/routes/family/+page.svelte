<script>
  // @ts-nocheck
  
  export const active = 'family';
  import Sidebar from '../sidebar/+page.svelte';
  import { userStore } from '../store';
  let familyMembers = [];
  let allUsers = [];
  let user = {};
  
  // Untuk mengambil data dari userStore
  userStore.subscribe(value => {
    user = value || {};
  });
  
  async function fetchFamilyMembers() {
    try {
      const response = await fetch(`http://127.0.0.1:8000/users/?family_email=${user.FamilyEmail}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      });
  
      if (response.ok) {
        const result = await response.json();
        familyMembers = result.users;
      } 
    } catch (error) {
      console.error("Error:", error);
    }
  }
  
  async function fetchAllUsers() {
    try {
      const response = await fetch(`http://127.0.0.1:8000/users/read-all-users`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      });
  
      if (response.ok) {
        const result = await response.json();
        allUsers = result.users;
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }
  
  async function deleteUser(UserID) {
    if (window.confirm("Apakah Anda yakin ingin menghapus pengguna ini?")) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/users/${UserID}`, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json'
          }
        });
  
        if (response.ok) {
          allUsers = allUsers.filter(user => user.UserID !== UserID);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    }
  }
  
  // Memanggil fungsi yang sesuai berdasarkan peran pengguna
  if (user.is_admin === 1) {
    fetchAllUsers();
  } else {
    fetchFamilyMembers();
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
    .family-members, .all-users {
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
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        border: 2px solid #000; /* Mempertebal garis tabel */
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
    }
    .delete-button {
        background-color: red;
        color: white;
        border: none;
        padding: 5px 10px;
        cursor: pointer;
        border-radius: 5px;
    }
    .delete-button:hover {
        background-color: darkred;
    }
  </style>
  
  <div class="layout">
    <div class="sidebar">
        <Sidebar active="family" />
    </div>
    <div class="content">
        
        {#if user.is_admin === 1}
          <h2>All Users</h2>
          <table>
            <thead>
              <tr>
                <th>UserID</th>
                <th>Username</th>
                <th>Fullname</th>
                <th>Gender</th>
                <th>Email</th>
                <th>Role</th>
                <th>FamilyEmail</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {#each allUsers as member}
                <tr>
                  <td>{member.UserID}</td>
                  <td>{member.Username}</td>
                  <td>{member.Fullname}</td>
                  <td>{member.Gender}</td>
                  <td>{member.Email}</td>
                  <td>{member.Role}</td>
                  <td>{member.FamilyEmail}</td>
                  <td><button class="delete-button" on:click={() => deleteUser(member.UserID)}>Delete</button></td>
                </tr>
              {/each}
            </tbody>
          </table>
        {:else}
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
        {/if}
    </div>
  </div>
  