<script>
  import { onMount } from 'svelte';
  import Sidebar from '../sidebar/+page.svelte';
  import { userStore } from '../store';

  export let active = 'detail-payment';
  let user = {};
  let transactions = [];

  // Subscribe to userStore to get user data
  userStore.subscribe(value => {
    user = value || {};
  });

  // Sample data for transactions for demonstration
  transactions = [
    { PaymentID: 1, TransactionID: 101, PaymentMethodID: 5, AmountPaid: 100, PaymentDate: '2024-06-29', Description: 'Payment for services' },
    // Add more sample transactions as needed
  ];

  function openModal() {
    const modal = document.getElementById("addModal");
    if (modal) {
      modal.classList.add("show");
    }
  }

  function closeModal() {
    const modal = document.getElementById("addModal");
    if (modal) {
      modal.classList.remove("show");
    }
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
  .header p {
    font-size: 14px;
    color: grey;
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
  .update {
    background-color: yellow; 
    color: black; 
  }
  .delete {
    background-color: red; 
    color: white;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  table th, table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  table th {
    background-color: #f2f2f2;
  }
  .download-btn {
    background-color: white;
    color: #4285F4;
    border: 1px solid #4285F4;
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
  }
  /* Modal Styles */
  .modal {
    display: none;
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
    margin: 10% auto;
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
  .modal.show {
    display: block;
  }
</style>

<div class="detail_payment">
  <Sidebar active="transaction" />
  <div class="content">
    <div class="header">
      <div>
        <h1>Hello {user.Fullname}</h1>
      </div>
    </div>

    <div>
      <h2>Recent Detail Payment</h2>
      <div class="buttons">
        <button class="add-button" on:click={openModal}>ADD</button>
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
          <th>Description</th>
          <th>Receipt</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {#each transactions as transaction}
          <tr>
            <td>{transaction.PaymentID}</td>
            <td>{transaction.TransactionID}</td>
            <td>{transaction.PaymentMethodID}</td>
            <td>{transaction.AmountPaid}</td>
            <td>{transaction.PaymentDate}</td>
            <td>{transaction.Description}</td>
            <td><button class="download-btn">Download</button></td>
            <td class="actions">
              <button class="update">UPDATE</button>
              <button class="delete">DELETE</button>
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
</div>

<!-- Modal -->
<div id="addModal" class="modal">
  <div class="modal-content">
    <span class="close" on:click={closeModal}>&times;</span>
    <h2>Add New Transaction</h2>
    <div class="form-group">
      <label for="paymentId">Payment ID</label>
      <input type="text" id="paymentId" name="paymentId" />
    </div>
    <div class="form-group">
      <label for="transactionId">Transaction ID</label>
      <input type="text" id="transactionId" name="transactionId" />
    </div>
    <div class="form-group">
      <label for="paymentMethodId">Payment Method ID</label>
      <input type="text" id="paymentMethodId" name="paymentMethodId" />
    </div>
    <div class="form-group">
      <label for="amountPaid">Amount Paid</label>
      <input type="text" id="amountPaid" name="amountPaid" />
    </div>
    <div class="form-group">
      <label for="paymentDate">Payment Date</label>
      <input type="date" id="paymentDate" name="paymentDate" />
    </div>
    <div class="form-group">
      <label for="description">Description</label>
      <input type="text" id="description" name="description" />
    </div>
    <button class="add-btn">ADD</button>
  </div>
</div>
