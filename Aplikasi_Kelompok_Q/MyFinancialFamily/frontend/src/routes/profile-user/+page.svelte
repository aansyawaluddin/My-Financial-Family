<script>
  // @ts-nocheck

  import Sidebar from '../sidebar/+page.svelte';
  import { userStore } from '../store';

  let user = {};
  let updatedUser = {};
  let showUpdatePopup = false;

  // Subscribe to the store to get user data
  userStore.subscribe(value => {
    user = value || {};
  });

  // Function to toggle the visibility of the update popup
  function toggleUpdatePopup() {
    showUpdatePopup = !showUpdatePopup;

    if (showUpdatePopup) {
      // Copy the user data to updatedUser when the popup is shown
      updatedUser = { ...user };
    }
  }

  // Function to update user data
  async function updateUser() {
    // Create an object with the updated user data
    const inputanForm = {
      UserID: user.UserID,
      Username: updatedUser.Username,
      Fullname: updatedUser.Fullname,
      Password: updatedUser.Password,
      Gender: updatedUser.Gender,
      Email: updatedUser.Email.toLowerCase(), // Convert email to lowercase
      Role: updatedUser.Role,
      FamilyEmail: updatedUser.FamilyEmail
    };

    // Validate input, ensure all fields are filled
    if (!updatedUser.Username || !updatedUser.Fullname || !updatedUser.Email || !updatedUser.Password || !updatedUser.Gender || !updatedUser.Role || !updatedUser.FamilyEmail) {
      alert("Please fill in all fields");
      return;
    }

    // Validate that the username is not longer than 10 characters
    if (updatedUser.Username.length > 10) {
      alert("Nickname cannot exceed 10 characters");
      return;
    }

    try {
      // Send a PUT request to update user data on the server
      const response = await fetch(`http://127.0.0.1:8000/users/${user.UserID}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(inputanForm)
      });

      if (response.ok) {
        const result = await response.json();
        userStore.set(result.user); // Update the user store with new data
        alert("Update User Success!");

      } else {
        alert("Failed to Update");
      }
    } catch (error) {
      console.error("Error:", error);
    }

    // Close the update popup after the update is done
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
    margin-top: 50px;
    text-align: center;
  }

  .profile-card h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }

  .profile-card p {
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    display: flex;
    justify-content: space-between;
  }

  .btn-update {
    background-color: #face6f;
    color: #fff;
    border: none;
    padding: 0.75rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 1rem;
    width: 100%;
    max-width: 200px; /* Limit maximum width */
    margin: 0 auto; /* Center button */
  }

  .btn-update:hover {
    background-color: #f8b82f;
  }

  .update-popup {
    position: fixed;
    top: 48%;
    left: 57%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    z-index: 1000;
    width: 80%; /* Overall width of the popup */
    max-width: 800px; /* Maximum width of the popup */
    display: grid;
    grid-template-columns: repeat(2, 1fr); /* Two columns of equal width */
    grid-gap: 1rem; /* Space between elements */
  }

  .update-popup h2 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
    grid-column: span 2; /* Span title across both columns */
  }

  .update-popup label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
  }

  .update-popup input,
  .update-popup select {
    width: calc(100% - 10px); /* Adjust width to input needs */
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
  }

  .update-popup .buttons {
    grid-column: span 1; /* Span buttons across both columns */
    display: flex;
    justify-content: space-between; /* Align buttons side by side */
  }

  .update-popup .btn-cancel,
  .update-popup .btn-update {
    width: calc(52% - 1rem); 
    margin-top: 15px;/* Equal width, with 0.5rem spacing in between */
    margin-bottom: 15px;/* Equal width, with 0.5rem spacing in between */
    border: none;
    border-radius: 4px;
    cursor: pointer;
    text-align: center;
  }

  .update-popup .btn-cancel {
    background-color: #fc8787;
    color: #fff;
  }

  .update-popup .btn-update {
    background-color: #face6f;
    color: #fff;
  }

  .update-popup .btn-cancel:hover {
    background-color: #fd4545;
  }

  .update-popup .btn-update:hover {
    background-color: #fcb419;
  }
</style>

<div class="page-profile">
  <Sidebar active="page-profile" />
  <div class="content">
    <div class="profile-card">
      <h2>Welcome, {user.Fullname}!</h2>
      <p><strong>User ID:</strong> {user.UserID}</p>
      <p><strong>Username:</strong> {user.Username}</p>
      <p><strong>Email:</strong> {user.Email}</p>
      <p><strong>Gender:</strong> {user.Gender}</p>
      <p><strong>Family Email:</strong> {user.FamilyEmail}</p>
      <p><strong>Role:</strong> {user.Role}</p>
      <button class="btn-update" on:click={toggleUpdatePopup}>Update Profile</button>
    </div>

    {#if showUpdatePopup}
      <div class="update-popup">
        <h2>Update Profile</h2>
        <div>
          <label for="username">Username</label>
          <input type="text" id="username" placeholder="Enter username" bind:value={updatedUser.Username} />
        </div>
        <div>
          <label for="fullname">Full Name</label>
          <input type="text" id="fullname" placeholder="Enter full name" bind:value={updatedUser.Fullname} />
        </div>
        <div>
          <label for="email">Email Address</label>
          <input type="email" id="email" placeholder="Enter email address" bind:value={updatedUser.Email} />
        </div>
        <div>
          <label for="password">Password</label>
          <input type="password" id="password" bind:value={updatedUser.Password} />
        </div>
        <div>
          <label for="gender">Gender</label>
          <select id="gender" bind:value={updatedUser.Gender}>
            <option value="">Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </div>
        <div>
          <label for="familyemail">Family Email</label>
          <input type="text" id="familyemail" placeholder="Enter family email" bind:value={updatedUser.FamilyEmail} />
        </div>
        <div>
          <label for="role">Role</label>
          <input type="text" id="role" placeholder="Enter role" bind:value={updatedUser.Role} />
        </div>
        <div class="buttons">
          <button class="btn-cancel" on:click={toggleUpdatePopup}>Cancel</button>
          <button class="btn-update" on:click={updateUser}>Update</button>
        </div>
      </div>
    {/if}
  </div>
</div>
