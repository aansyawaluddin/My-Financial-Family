<script>
  // @ts-nocheck
  import { onMount } from 'svelte';
  import Sidebar from '../sidebar/+page.svelte';
  import { userStore } from '../store';

  export let active = 'detail-payment';
  let user = {};
  let detailpayments = [];
  let transactions = [];
  let selectedTransactionId = ''; // For binding selected transaction ID
  let paymentMethods = []; // To store payment methods
  let currentDetailPayment = {}; // For holding the current detail payment to update

  // Subscribe to userStore to get user data
  userStore.subscribe(value => {
    user = value || {};
  });

  onMount(async () => {
    await readDetailPayments(); // Fetch detail payments when component mounts
    await readTransaction(); // Fetch transactions when component mounts
    await fetchPaymentMethods(); // Fetch payment methods when component mounts
  });

  async function readDetailPayments() {
    try {
      const response = await fetch('http://localhost:8000/detail-payments/read-all-detailpayment', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
      });

      if (response.ok) {
        const result = await response.json();
        detailpayments = result.detail_payments;
      } else {
        detailpayments = [];
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  async function readTransaction() {
    try {
      const response = await fetch(`http://localhost:8000/transactions/${user.UserID}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
      });

      if (response.ok) {
        const result = await response.json();
        transactions = result.transactions;
      } else {
        transactions = [];
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  async function fetchPaymentMethods() {
    try {
      const response = await fetch('http://localhost:8000/payment_methods/read-all-method', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
      });

      if (response.ok) {
        const result = await response.json();
        paymentMethods = result.methods;
      } else {
        console.error('Failed to fetch payment methods');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  async function addDetailPayment() {
    const newDetailPayment = {
      TransactionID: selectedTransactionId,
      PaymentMethodID: document.getElementById('paymentMethodId').value,
      AmountPaid: document.getElementById('amountPaid').value,
      PaymentDate: document.getElementById('paymentDate').value,
    };

    try {
      const response = await fetch('http://localhost:8000/detail-payments', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(newDetailPayment)
      });

      if (response.ok) {
        const result = await response.json();
        await readDetailPayments(); // Refresh the detail payments list
        closeModal(); // Close modal after adding
      } else {
        console.error('Failed to add detail payment');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  async function updateDetailPayment() {
    const updatedDetailPayment = {
      TransactionID: document.getElementById('updateTransactionId').value,
      PaymentMethodID: document.getElementById('updatePaymentMethodId').value,
      AmountPaid: document.getElementById('updateAmountPaid').value,
      PaymentDate: document.getElementById('updatePaymentDate').value,
    };

    try {
      const response = await fetch(`http://localhost:8000/detail-payments/${currentDetailPayment.PaymentID}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedDetailPayment)
      });

      if (response.ok) {
        const result = await response.json();
        await readDetailPayments(); // Refresh the detail payments list
        closeModal(); // Close modal after updating
      } else {
        console.error('Failed to update detail payment');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  async function deleteDetailPayment(paymentID) {
    try {
      const response = await fetch(`http://localhost:8000/detail-payments/${paymentID}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        await readDetailPayments(); // Refresh the detail payments list
      } else {
        console.error('Failed to delete detail payment');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  function openAddModal() {
    const modal = document.getElementById('addModal');
    if (modal) {
      modal.style.display = 'block'; // Show modal
    }
  }

  function openUpdateModal(detailPayment) {
    currentDetailPayment = detailPayment;
    const modal = document.getElementById('updateModal');
    if (modal) {
      modal.style.display = 'block'; // Show modal
    }
  }

  function closeModal() {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => modal.style.display = 'none'); // Hide all modals
  }
</script>

<style>
  .detail_payment {
    display: flex;
    height: 100vh;
    box-sizing: border-box;
  }
  .content {
    flex: 1;
    padding: 1rem;
    overflow-y: auto;
    margin-left: 180px;
  }
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
  }
  .header h1 {
    font-size: 24px;
  }
  .buttons {
    display: flex;
    gap: 10px;
  }
  .buttons button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  .add-button {
    background-color: #4285F4;
    color: white;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  table th,
  table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  table th {
    background-color: #f2f2f2;
  }
  .modal {
    display: none; /* Initially hide the modal */
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000;
    overflow: auto;
  }
  .modal-content {
    background-color: white;
    margin: 1% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
    max-width: 400px;
    border-radius: 10px;
  }
  .close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
  }
  .close:hover,
  .close:focus {
    color: black;
    text-decoration: none;
  }
  .form-group {
    margin-bottom: 1rem;
  }
  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
  }
  .form-group input,
  .form-group select {
    width: 100%;
    padding: 0.5rem;
    box-sizing: border-box;
  }
  .add-btn {
    display: block;
    width: 100%;
    padding: 0.75rem;
    background-color: #4285F4;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  .update {
    background-color: yellow;
    color: black;
  }
  .delete {
    background-color: red;
    color: white;
  }
</style>

<div class="detail_payment">
  <Sidebar active="detail-payment" />
  <div class="content">
    <div class="header">
      <div>
        <h1>Hello {user.Fullname}</h1>
      </div>
    </div>

    <div>
      <h2>Detail Payment</h2>
      <div class="buttons">
        <button class="add-button" on:click={openAddModal}>ADD</button>
      </div>
    </div>

    <table>
      <thead>
        <tr>
          <th>PaymentID</th>
          <th>TransactionID</th>
          <th>PaymentMethodID</th>
          <th>AmountPaid</th>
          <th>PaymentDate</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {#each detailpayments as detailpayment}
        <tr>
          <td>{detailpayment.PaymentID}</td>
          <td>{detailpayment.TransactionID}</td>
          <td>{detailpayment.PaymentMethodID}</td>
          <td>{detailpayment.AmountPaid}</td>
          <td>{detailpayment.PaymentDate}</td>
          <td class="actions">
            <button class="update" on:click={() => openUpdateModal(detailpayment)}>UPDATE</button>
            <button class="delete" on:click={() => deleteDetailPayment(detailpayment.PaymentID)}>DELETE</button>
          </td>
        </tr>
        {/each}
      </tbody>
    </table>
  </div>
</div>

<!-- Add Modal -->
<div id="addModal" class="modal">
  <div class="modal-content">
    <span class="close" on:click={closeModal}>&times;</span>
    <h2>Add New Detail Payment</h2>
    <div class="form-group">
      <label for="transactionId">Transaction ID</label>
      <select id="transactionId" name="transactionId" bind:value={selectedTransactionId}>
        {#each transactions as transaction}
        <option value={transaction.TransactionID}>{transaction.Description}</option>
        {/each}
      </select>
    </div>
    <div class="form-group">
      <label for="paymentMethodId">Payment Method ID</label>
      <select id="paymentMethodId" name="paymentMethodId">
        {#each paymentMethods as method}
        <option value={method.MethodID}>{method.MethodName}</option>
        {/each}
      </select>
    </div>
    <div class="form-group">
      <label for="amountPaid">Amount Paid</label>
      <input type="number" id="amountPaid" name="amountPaid" />
    </div>
    <div class="form-group">
      <label for="paymentDate">Payment Date</label>
      <input type="date" id="paymentDate" name="paymentDate" />
    </div>
    <button class="add-btn" on:click={addDetailPayment}>ADD</button>
  </div>
</div>

<!-- Update Modal -->
<div id="updateModal" class="modal">
  <div class="modal-content">
    <span class="close" on:click={closeModal}>&times;</span>
    <h2>Update Detail Payment</h2>
    <div class="form-group">
      <label for="updateTransactionId">Transaction ID</label>
      <select id="updateTransactionId" name="transactionId" bind:value={currentDetailPayment.TransactionID}>
        {#each transactions as transaction}
        <option value={transaction.TransactionID}>{transaction.Description}</option>
        {/each}
      </select>
    </div>
    <div class="form-group">
      <label for="updatePaymentMethodId">Payment Method ID</label>
      <select id="updatePaymentMethodId" name="updatePaymentMethodId" bind:value={currentDetailPayment.PaymentMethodID}>
        {#each paymentMethods as method}
        <option value={method.MethodID}>{method.MethodName}</option>
        {/each}
      </select>
    </div>
    <div class="form-group">
      <label for="updateAmountPaid">Amount Paid</label>
      <input type="number" id="updateAmountPaid" name="updateAmountPaid" bind:value={currentDetailPayment.AmountPaid} />
    </div>
    <div class="form-group">
      <label for="updatePaymentDate">Payment Date</label>
      <input type="date" id="updatePaymentDate" name="updatePaymentDate" bind:value={currentDetailPayment.PaymentDate} />
    </div>
    <button class="add-btn" on:click={updateDetailPayment}>UPDATE</button>
  </div>
</div>
