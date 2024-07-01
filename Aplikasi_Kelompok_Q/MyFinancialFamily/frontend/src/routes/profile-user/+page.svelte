<script>
  // @ts-nocheck
  
  import Sidebar from '../sidebar/+page.svelte';
  import { userStore } from '../store';
  
  let user = {};
  let updatedUser = {};
  let showUpdatePopup = false;
  let isPasswordChanged = false;  // New flag to track password changes
  
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
      isPasswordChanged = false;  // Reset flag when opening the popup
    }
  }
  
  // Function to update user data
  async function updateUser() {
    // Create an object with the updated user data
    const inputanForm = {
      UserID: user.UserID,
      Username: updatedUser.Username,
      Fullname: updatedUser.Fullname,
      Password: isPasswordChanged ? updatedUser.Password : user.Password, // Use the original password if not changed
      Gender: updatedUser.Gender,
      Email: updatedUser.Email.toLowerCase(), // Convert email to lowercase
      Role: updatedUser.Role,
    };
  
    // Validate input, ensure all fields are filled
    if (!updatedUser.Username || !updatedUser.Fullname || !updatedUser.Email || !updatedUser.Password || !updatedUser.Gender || !updatedUser.Role ) {
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
  .sidebar {
    width: 288px;
    flex-shrink: 0;
  }
  .content {
    flex: 1;
    padding: 1rem;
    overflow-y: auto;
  }

  .profile-card {
    background-color: #fff;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    text-align: center;
    margin: 50px auto; 
  }

  .profile-card h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }

  .profile-card p {
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    text-align: left; 
  }

  .btn-update {
    width: 100%;
    max-width: 200px;
    margin: 0 auto;
  }
  /* Update popup */
  .update-popup {
    position: absolute;
    top: 50%;
    left: 50%;
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

    .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    z-index: 999;
    display: none;
  }

  .show-overlay {
    display: block;
  }
  .d-md-flex {
      display: flex;
      justify-content: center;
      align-items: center;
      grid-column: span 2;
    }

</style>

<div class="page-profile">
  <div class="sidebar">
    <Sidebar active="page-profile" />
  </div>
  <div class="content">
    <div class="profile-card">
      {#if user.is_admin === 1}
        <h2 class="mb-4">Profile Information (Admin)</h2>
      {:else}
        <h2 class="mb-4">Profile Information</h2>
      {/if}
      <p class="mb-2"><strong>User ID:</strong> {user.UserID}</p>
      <p class="mb-2"><strong>Username:</strong> {user.Username}</p>
      <p class="mb-2"><strong>Fullname:</strong> {user.Fullname}</p>
      <p class="mb-2"><strong>Email:</strong> {user.Email}</p>
      <p class="mb-2"><strong>Gender:</strong> {user.Gender}</p>
      <p class="mb-4"><strong>Role:</strong> {user.Role}</p>
      <button class="btn btn-warning btn-update mb-4" on:click={toggleUpdatePopup}>Update Profile</button>
    </div>

    {#if showUpdatePopup}
    <div class="overlay show-overlay"></div>
    <div class="update-popup bg-light p-4 rounded shadow-lg">
      <h2 class="mb-4">Update Profile</h2>
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" class="form-control" id="username" placeholder="Enter username" bind:value={updatedUser.Username} />
      </div>
      <div class="mb-3">
        <label for="fullname" class="form-label">Full Name</label>
        <input type="text" class="form-control" id="fullname" placeholder="Enter full name" bind:value={updatedUser.Fullname} />
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email Address</label>
        <input type="email" class="form-control" id="email" placeholder="Enter email address" bind:value={updatedUser.Email} />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" id="password" bind:value={updatedUser.Password} on:input={() => isPasswordChanged = true} />
      </div>
      <div class="mb-3">
        <label for="gender" class="form-label">Gender</label>
        <select id="gender" class="form-select" bind:value={updatedUser.Gender}>
          <option value="">Select Gender</option>
          <option value="Male">Male</option>
          <option value="Female">Female</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="role" class="form-label">Role</label>
        <input type="text" class="form-control" id="role" placeholder="Enter role" bind:value={updatedUser.Role} />
      </div>
      <div class="d-md-flex justify-content-md-end align-items-center">
        <button class="btn btn-danger me-md-2 mb-2 mb-md-0" on:click={toggleUpdatePopup}>Cancel</button>
        <button class="btn btn-success" on:click={updateUser}>Update</button>
      </div>
    </div>
    {/if}
  </div>
</div>
