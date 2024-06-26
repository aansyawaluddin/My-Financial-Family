<script>
  // @ts-nocheck
  import { onMount } from 'svelte';
  import Sidebar from '../sidebar/+page.svelte';
  import { userStore } from '../store';

  export const active = 'transaction';

  let user = {};
  let transactions = [];
  let showModal = false;
  let showUpdateModal = false;
  let categories = [];
  let selectedTransaction = null;

  // Form inputs
  let expensescategoryid= 0;
  let amount;
  let transactiondate = '';
  let description = '';

  // Subscribe untuk mengambil data pengguna dari userStore
  userStore.subscribe(value => {
    user = value || {};
  });

  async function fetchCategories() {
    try {
      const response = await fetch('http://localhost:8000/categories/read-all-categories', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        const result = await response.json();
        categories = result.categories;
      } else {
        categories = []
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  async function readTransactions() {
    try {
      const response = await fetch('http://localhost:8000/transactions/read-all-transactions', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        const result = await response.json();
        transactions = result.transactions;
      } else {
        transactions = []
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  onMount(() => {
    readTransactions();
    fetchCategories();
  });

  function openModal() {
    showModal = true;
  }

  function closeModal() {
    showModal = false;
  }

  function openUpdateModal(transaction) {
    selectedTransaction = transaction;
    expensescategoryid = transaction.ExpensesCategoryID;
    amount = transaction.Amount;
    transactiondate = transaction.TransactionDate;
    description = transaction.Description;
    showUpdateModal = true;
  }

  function closeUpdateModal() {
    showUpdateModal = false;
    selectedTransaction = null;
  }

  async function addTransaction() {
    const newTransaction = {
      UserID: user.UserID,
      ExpensesCategoryID: expensescategoryid,
      Amount: amount,
      TransactionDate: transactiondate,
      Description: description
    };
    if (!expensescategoryid || !amount || !transactiondate || !description ) {
      alert("Silakan isi semua bidang");
      return;
    }
    if (amount < 1000) {
      alert("nominal sangat kecil (minimal 1000 perak)");
      return;
    }

    try {
      const response = await fetch(`http://localhost:8000/transactions`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(newTransaction)
      });

      if (response.ok) {
        // If transaction addd successfully, close the modal and refresh transactions
        closeModal();
        readTransactions();
      } else {
        console.error('Failed to add transaction');
      }
    } catch (error) {
      console.error('Error saving transaction:', error);
    }
  }

  async function updateTransaction(transactionID) {
    if (!selectedTransaction) return;

    const updatedTransaction = {
      ExpensesCategoryID: expensescategoryid,
      Amount: amount,
      TransactionDate: transactiondate,
      Description: description
    };

    try {
      const response = await fetch(`http://localhost:8000/transactions/transactions/${transactionID}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedTransaction)
      });

      if (response.ok) {
        closeUpdateModal();
        readTransactions();
      } else {
        console.error('Failed to update transaction');
      }
    } catch (error) {
      console.error('Error updating transaction:', error);
    }
  }

  async function deleteTransaction(transactionID) {
    const confirmation = confirm("Are you sure you want to delete this transaction?");
    if (!confirmation) return;

    try {
      const response = await fetch(`http://localhost:8000/transactions/${transactionID}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        readTransactions(); // Refresh transactions after deletion
      } else {
        console.error('Failed to delete transaction');
      }
    } catch (error) {
      console.error('Error deleting transaction:', error);
    }
  }
</script>

<style>
  .transaction {
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
  .buttons .add {
    background-color: #4285F4;
    color: white;
  }
  .buttons .update {
    background-color: yellow; 
    color: black; 
  }
  .buttons .delete {
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

<div class="transaction">
  <Sidebar active="transaction" />
  <div class="content">
    <div class="header">
      <div>
        <h1>Hello {categories.CategoryID}</h1>
      </div>
    </div>

    <div>
      <h2>Recent Transactions</h2>
      <div class="buttons">
        <button class="add" on:click={openModal}>ADD</button>
      </div>
    </div>

    <table>
      <thead>
        <tr>
          <th>TransactionID</th>
          <th>UserID</th>
          <th>ExpensesCategoryID</th>
          <th>Amount</th>
          <th>TransactionDate</th>
          <th>Description</th>
          <th>Receipt</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {#each transactions as transaction}
          <tr>
            <td>{transaction.TransactionID}</td>
            <td>{transaction.UserID}</td>
            <td>{transaction.ExpensesCategoryID}</td>
                        <td>{transaction.Amount}</td>
            <td>{transaction.TransactionDate}</td>
            <td>{transaction.Description}</td>
            <td><button class="download-btn">Download</button></td>
            <td>
              <button class="update" on:click={() => openUpdateModal(transaction)}>UPDATE</button>
              <button class="delete" on:click={() => deleteTransaction(transaction.TransactionID)}>DELETE</button>
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>

  <div class:modal={true} class:show={showModal}>
    <div class="modal-content">
      <span class="close" on:click={closeModal}>&times;</span>
      <div class="form-group">
        <label for="category">Category</label>
        <select id="category" bind:value={expensescategoryid}>
          <option value="">Select a category</option>
          {#each categories as category}
            <option value={category.CategoryID}>{category.CategoryName}</option>
          {/each}
        </select>
      </div>
      <div class="form-group">
        <label for="amount">Amount</label>
        <input type="text" id="amount" placeholder="Input Here" bind:value={amount}>
      </div>
      <div class="form-group">
        <label for="transaction-date">Transaction Date</label>
        <input type="date" id="transaction-date" bind:value={transactiondate}>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <input type="text" id="description" placeholder="Input Here" bind:value={description}>
      </div>
      <button class="add-btn" on:click={addTransaction}>Add Categories</button>
    </div>
  </div>

  <div class:modal={true} class:show={showUpdateModal}>
  <div class="modal-content">
    <span class="close" on:click={closeUpdateModal}>&times;</span>
    <div class="form-group">
      <label for="category">Category</label>
      <select id="category" bind:value={expensescategoryid}>
        <option value="">Select a category</option>
        {#each categories as category}
          <option value={category.CategoryID}>{category.CategoryName}</option>
        {/each}
      </select>
    </div>
    <div class="form-group">
      <label for="amount">Amount</label>
      <input type="text" id="amount" placeholder="Input Here" bind:value={amount}>
    </div>
    <div class="form-group">
      <label for="transaction-date">Transaction Date</label>
      <input type="date" id="transaction-date" bind:value={transactiondate}>
    </div>
    <div class="form-group">
      <label for="description">Description</label>
      <input type="text" id="description" placeholder="Input Here" bind:value={description}>
    </div>
    <button class="add-btn" on:click={() => updateTransaction(selectedTransaction.TransactionID)}>Update Transaction</button>
  </div>
</div>
</div>