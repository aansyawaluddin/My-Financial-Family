<script>
  import Sidebar from '../sidebar/+page.svelte';

  export const active = 'transaction';

  let transactions = [
    { description: "Spotify Subscription", transactionId: "#12548796", type: "Shopping", card: "1234 ****", date: "28 Jan, 12.30 AM", amount: "$2,500" },
    { description: "Freepik Sales", transactionId: "#12548796", type: "Transfer", card: "1234 ****", date: "25 Jan, 10.40 PM", amount: "$750" },
    { description: "Mobile Service", transactionId: "#12548796", type: "Service", card: "1234 ****", date: "20 Jan, 10.40 PM", amount: "$150" },
    { description: "Wilson", transactionId: "#12548796", type: "Transfer", card: "1234 ****", date: "15 Jan, 03.29 PM", amount: "$1050" },
    { description: "Emilly", transactionId: "#12548796", type: "Transfer", card: "1234 ****", date: "14 Jan, 10.40 PM", amount: "$840" },
  ];

  let showModal = false;

  function openModal() {
    showModal = true;
  }

  function closeModal() {
    showModal = false;
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
    margin-left: 180px; /* Sesuaikan dengan lebar sidebar */
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
    background-color: #FBBC05;
    color: white;
  }
  .buttons .delete {
    background-color: #EA4335;
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
  .save-btn {
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
        <h1>Hello mr.haikal</h1>
        <p>May 19, 2024</p>
      </div>
    </div>

    <div>
      <h2>Recent Transactions</h2>
      <div class="buttons">
        <button class="add" on:click={openModal}>ADD</button>
        <button class="update">UPDATE</button>
        <button class="delete">DELETE</button>
      </div>
    </div>

    <table>
      <thead>
        <tr>
          <th>Description</th>
          <th>Transaction ID</th>
          <th>Type</th>
          <th>Card</th>
          <th>Date</th>
          <th>Amount</th>
          <th>Receipt</th>
        </tr>
      </thead>
      <tbody>
        {#each transactions as transaction}
          <tr>
            <td>{transaction.description}</td>
            <td>{transaction.transactionId}</td>
            <td>{transaction.type}</td>
            <td>{transaction.card}</td>
            <td>{transaction.date}</td>
            <td>{transaction.amount}</td>
            <td><button class="download-btn">Download</button></td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>

  <div class:modal={true} class:show={showModal}>
    <div class="modal-content">
      <span class="close" on:click={closeModal}>&times;</span>
      <div class="form-group">
        <label for="user">User</label>
        <select id="user">
          <option>Select a user</option>
        </select>
      </div>
      <div class="form-group">
        <label for="category">Category</label>
        <select id="category">
          <option>Select a category</option>
        </select>
      </div>
      <div class="form-group">
        <label for="payment-method">Payment Method</label>
        <select id="payment-method">
          <option>Select a method</option>
        </select>
      </div>
      <div class="form-group">
        <label for="amount">Amount</label>
        <input type="text" id="amount" placeholder="Input Here">
      </div>
      <div class="form-group">
        <label for="transaction-date">Transaction Date</label>
        <input type="text" id="transaction-date" placeholder="YYYY/MM/DD">
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <input type="text" id="description" placeholder="Input Here">
      </div>
      <button class="save-btn">Save</button>
    </div>
  </div>
</div>