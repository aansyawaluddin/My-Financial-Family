<script>
  // @ts-nocheck
  
  import { userStore } from '../store';
  import Sidebar from '../sidebar/+page.svelte';

  let user = {};
  let familyMembers = [];
  
  // Subscribe untuk mengambil data pengguna dari userStore
  userStore.subscribe(value => {
    user = value ;
  });

  // Function untuk membaca data semua pengguna
  async function ReadData() {
    try {
      const response = await fetch(`http://127.0.0.1:8000/users/read-all-users`, {
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

  // Function untuk menghapus pengguna
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
          familyMembers = familyMembers.filter(member => member.UserID !== UserID);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    }
  }

  // Memanggil fungsi ReadData saat komponen dimuat
  ReadData();
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
  }
  .content h1{
    flex-grow: 1;
    padding: 20px;
    margin-left: 200px;
  }
  .family-members {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: left; /* Memusatkan semua card */
  }
  .card {
    width: 250px;
    height: 220px; /* Tambahkan sedikit tinggi untuk memberi ruang bagi tombol delete */
    box-sizing: border-box;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: space-between; /* Agar konten di tengah dan tombol delete di atas */
  }
  .card img {
    border-radius: 50%;
    width: 100px;
    height: 100px;
    margin: 0 auto; /* Memastikan gambar berada di tengah */
  }
  .card .name {
    font-weight: bold;
    margin-top: 10px;
  }
  .card .role {
    color: gray;
  }
  .delete-button {
    background-color: red;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 5px;
    align-self: flex-end; /* Mengatur tombol delete ke ujung kanan atas */
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
    <h1>Hello, {user.Fullname}</h1>
    <h2>Family Members</h2>
    <div class="family-members">
      {#each familyMembers as member}
        <div class="card">
          {#if user.is_admin === 1 && user.UserID !== member.UserID}
            <button class="delete-button" on:click={() => deleteUser(member.UserID)}>Delete</button>
          {/if}
          <img src="https://i.pinimg.com/474x/a3/f4/bc/a3f4bc0dc7d1b030b782c62d7a4781cf.jpg" alt={member.Fullname} />
          <div class="name">{member.Fullname} {#if member.is_admin === 1}(Admin){/if}</div>
          <div class="role">{member.Role}</div>
        </div>
      {/each}
    </div>
  </div>
</div>
