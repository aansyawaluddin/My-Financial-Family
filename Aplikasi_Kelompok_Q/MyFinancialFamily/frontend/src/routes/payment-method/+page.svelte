<script>
  // @ts-nocheck
  export const active = 'payment-method';
  import Sidebar from '../sidebar/+page.svelte';
  import { onMount } from 'svelte';
  import { userStore } from '../store';
  let user = {};

  // Subscribe untuk mengambil data pengguna dari userStore
  userStore.subscribe(value => {
    user = value || {};
  });

  // State variables
  let showModal = false;
  let showUpdateModal = false;
  let showDeleteModal = false;
  let paymentMethodName = '';
  let paymentMethods = [];
  let selectedMethod = null; // To store the selected method for updating or deleting

  // Function to add a new payment method
  async function addPaymentMethod() {
    try {
      const response = await fetch('http://localhost:8000/payment_methods/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ MethodName: paymentMethodName })
      });

      if (response.ok) {
        closeModal(); // Close modal after successful addition
        await fetchPaymentMethods(); // Refresh payment methods list
      } else {
        console.error('Failed to create payment method');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  // Function to fetch all payment methods
  async function fetchPaymentMethods() {
    try {
      const response = await fetch('http://localhost:8000/payment_methods/read-all-methods', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        const result = await response.json();
        paymentMethods = result.methods;
      } else {
        paymentMethods = []
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  // Function to update a payment method
  async function updatePaymentMethod() {
    try {
      const response = await fetch(`http://localhost:8000/payment_methods/${selectedMethod.MethodID}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ MethodName: selectedMethod.MethodName })
      });

      if (response.ok) {
        closeUpdateModal(); // Close modal after successful update
        await fetchPaymentMethods(); // Refresh payment methods list
      } else {
        console.error('Failed to update payment method');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  // Function to delete a payment method
  async function deletePaymentMethod() {
    try {
      const response = await fetch(`http://localhost:8000/payment_methods/${selectedMethod.MethodID}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        closeDeleteModal(); // Close modal after successful deletion
        await fetchPaymentMethods(); // Refresh payment methods list
      } else {
        console.error('Failed to delete payment method');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  // Function to open modal
  function openModal() {
    showModal = true;
  }

  // Function to close modal
  function closeModal() {
    showModal = false;
    paymentMethodName = ''; // Reset paymentMethodName when modal is closed
  }

  // Function to open update modal
  function openUpdateModal(method) {
    selectedMethod = { ...method }; // Menampilkan method lama di kolom pengisian
    showUpdateModal = true;
  }

  // Function to close update modal
  function closeUpdateModal() {
    showUpdateModal = false;
    selectedMethod = null; // Reset selected method
  }

  // Function to open delete modal
  function openDeleteModal(method) {
    selectedMethod = { ...method }; // Menyimpan method yang akan dihapus
    showDeleteModal = true;
  }

  // Function to close delete modal
  function closeDeleteModal() {
    showDeleteModal = false;
    selectedMethod = null; // Reset selected method
  }

  // Fetch payment methods on component mount
  onMount(fetchPaymentMethods);
</script>

<style>
  .payment-method {
    display: flex;
    height: 100vh;
    box-sizing: border-box;
  }
  .sidebar {
    position: fixed;
    z-index: 100;
  }
  .content {
    flex: 1;
    padding: 1rem;
    overflow-y: auto;
    margin-left: 200px; /* Adjust based on sidebar width */
  }
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }
  .buttons {
    display: flex;
    gap: 0.5rem;
  }
  .card-container {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
  }
  .card {
    display: flex;
    flex-direction: column; /* Changed to column layout */
    align-items: center;
    padding: 1rem;
    background: white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-radius: 0.5rem;
    width: 200px;
    justify-content: space-between;
    margin-bottom: 1rem;
  }
  .card img {
    width: 60px;
    height: 60px;
    margin-top: 10px;
  }
  .card h3 {
    margin: 0;
    margin-top: 20px;
    font-size: 1.2rem;
  }
  .card-arrow {
    margin-left: auto;
  }
  button {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.5rem;
    cursor: pointer;
  }
  .add-button {
    background-color: #007bff;
    color: white;
  }
  .update-button {
    padding: 3px 3px;
    font-size: 12px;
    background-color: #ffc107;
    color: white;
    margin-left: 70px;
  }
  .delete-button {
    padding: 3px 3px;
    font-size: 12px;
    background-color: #dc3545;
    color: white;
  }
  /* Modal styles */
  .modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1000;
  }
  .modal-content {
    background: white;
    padding: 1rem;
    border-radius: 0.5rem;
    width: 300px;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  .modal-header,
  .modal-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .modal-header h2 {
    margin: 0;
  }
  .modal-body input {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 0.5rem;
  }
</style>

<div class="payment-method">
  <div class="sidebar">
    <Sidebar active="payment-method" />
  </div>
  <div class="content">
    <div class="header">
      <h1>Payment Methods</h1>
      {#if user.is_admin === 1}
      <div class="buttons">
        <button class="add-button" on:click={openModal}>ADD</button>
      </div>
      {/if}
    </div>
    <div class="card-container">
      {#each paymentMethods as method}
        <div class="card">
          {#if user.is_admin === 1}
          <div class="buttons">
            <button class="update-button" on:click={() => openUpdateModal(method)}>UPDATE</button>
            <button class="delete-button" on:click={() => openDeleteModal(method)}>DELETE</button>
          </div>
          {/if}
          <img src="https://i.pinimg.com/564x/fe/99/c7/fe99c72499b9be5c1f79a33b06b3d4e1.jpg" alt={method.MethodName}>
          <h3>{method.MethodName}</h3>
        </div>
      {/each}
    </div>
  </div>

  {#if showModal}
  <div class="modal" on:click={closeModal}>
    <div class="modal-content" on:click|stopPropagation>
      <div class="modal-header">
        <h2>Add Payment Method</h2>
        <button on:click={closeModal}>Close</button>
      </div>
      <div class="modal-body">
        <input type="text" placeholder="Payment Category Name" bind:value={paymentMethodName} />
      </div>
      <div class="modal-footer">
        <button on:click={addPaymentMethod}>Save</button>
        <button on:click={closeModal}>Cancel</button>
      </div>
    </div>
  </div>
  {/if}

  {#if showUpdateModal}
  <div class="modal" on:click={closeUpdateModal}>
    <div class="modal-content" on:click|stopPropagation>
      <div class="modal-header">
        <h2>Update Payment Method</h2>
        <button on:click={closeUpdateModal}>Close</button>
      </div>
      <div class="modal-body">
        <input type="text" placeholder="Payment Category Name" bind:value={selectedMethod.MethodName} />
      </div>
      <div class="modal-footer">
        <button on:click={updatePaymentMethod}>Save</button>
        <button on:click={closeUpdateModal}>Cancel</button>
      </div>
    </div>
  </div>
  {/if}

  {#if showDeleteModal}
  <div class="modal" on:click={closeDeleteModal}>
    <div class="modal-content" on:click|stopPropagation>
      <div class="modal-header">
        <h2>Delete Payment Method</h2>
        <button on:click={closeDeleteModal}>Close</button>
      </div>
      <div class="modal-body">
        <p>Are you sure you want to delete the payment method "{selectedMethod.MethodName}"?</p>
      </div>
      <div class="modal-footer">
        <button on:click={deletePaymentMethod}>Yes</button>
        <button on:click={closeDeleteModal}>No</button>
      </div>
    </div>
  </div>
  {/if}
</div>
