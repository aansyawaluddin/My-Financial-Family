<!-- src/Sidebar.svelte -->
<script>
  // @ts-nocheck

  import Sidebar from '../sidebar/+page.svelte';
  import { userStore } from '../store';

  let user = {};
  let showUpdatePopup = false;

  // Subscribe to the store to get user data
  userStore.subscribe(value => {
    user = value || {};
  });

  function toggleUpdatePopup() {
    showUpdatePopup = !showUpdatePopup;
  }

  function updateUser() {
    // Simulasikan proses update data user
    // Misalnya, lakukan permintaan HTTP ke backend untuk menyimpan perubahan data user
    console.log("Update user data here...");
    // Setelah proses update selesai, Anda dapat menutup pop-up jika diperlukan
    showUpdatePopup = false;
  }
</script>

<style>
  .page-profile {
    display: flex;
    height: 100vh;
    box-sizing: border-box;
  }

  .content {
    flex: 1;
    padding: 1rem;
    margin-left: 50px;
    overflow-y: auto;
  }

  .profile-card {
    background-color: #fff;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    margin-left: 190px;
    margin-top: 70px;
    text-align: center;
  }

  .profile-card h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }

  .profile-card p {
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
  }

  .btn-update {
    background-color: #face6f;
    color: #fff;
    border: none;
    padding: 0.75rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 1rem;
  }

  .btn-update:hover {
    background-color: #f8b82f;
  }

  .update-popup {
    position: fixed;
    top: 50%;
    left: 57%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    z-index: 1000;
    width: 80%; /* Lebar keseluruhan popup */
    max-width: 800px; /* Atur lebar maksimum popup */
    display: grid;
    grid-template-columns: repeat(2, 1fr); /* Dua kolom dengan lebar sama */
    grid-gap: 1rem; /* Jarak antar elemen */
  }

  .update-popup h2 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
    grid-column: span 2; /* Menyatukan judul di kedua kolom */
  }

  .update-popup label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
  }

  .update-popup input,
  .update-popup select {
    width: calc(100% - 10px); /* Sesuaikan dengan kebutuhan lebar input */
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
  }

  .update-popup .btn-cancel {
    background-color: #fc8787;
    color: #fff;
    border: none;
    padding: 0.75rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    margin-right: 1rem;
  }

  .update-popup .btn-update {
    background-color: #face6f;
    color: #fff;
    border: none;
    padding: 0.75rem 1rem;
    border-radius: 4px;
    cursor: pointer;
  }

  .update-popup .btn-update:hover {
    background-color: #fcb419;
  }
  .update-popup .btn-cancel:hover {
    background-color: #fd4545;
  }
</style>

<div class="page-profile">
  <Sidebar active="page-profile" />
  <div class="content">
    <div class="profile-card">
      <h2>Welcome, {user.Fullname}!</h2>
      <p>User ID: {user.UserID}</p>
      <p>Email: {user.Email}</p>
      <p>Gender: {user.Gender}</p>
      <p>Family Email: {user.FamilyEmail}</p>
      <p>Role: {user.Role}</p>
      <button class="btn-update" on:click={toggleUpdatePopup}>Update Profile</button>
    </div>

    {#if showUpdatePopup}
      <div class="update-popup">
        <h2>Update Profile</h2>
        <div>
          <label for="username">Username</label>
          <input type="text" id="username" placeholder="Enter username" bind:value={user.Username} />
        </div>
        <div>
          <label for="fullname">Full Name</label>
          <input type="text" id="fullname" placeholder="Enter full name" bind:value={user.Fullname} />
        </div>
        <div>
          <label for="email">Email Address</label>
          <input type="email" id="email" placeholder="Enter email address" bind:value={user.Email} />
        </div>
        <div>
          <label for="password">Password</label>
          <input type="password" id="password"  bind:value={user.Password} />
        </div>
        <div>
          <label for="gender">Gender</label>
          <select id="gender" bind:value={user.Gender}>
            <option value="">Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </div>
        <div>
          <label for="familyemail">Family Email</label>
          <input type="text" id="familyemail" placeholder="Enter family email" bind:value={user.FamilyEmail} />
        </div>
        <div>
          <label for="role">Role</label>
          <input type="text" id="role" placeholder="Enter role" bind:value={user.Role} />
        </div>
        <div class="buttons">
          <button class="btn-cancel" on:click={toggleUpdatePopup}>Cancel</button>
          <button class="btn-update" on:click={updateUser}>Update</button>
        </div>
      </div>
    {/if}
  </div>
</div>
