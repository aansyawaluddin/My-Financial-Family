<script>
  export const active = 'transaction';
  import Sidebar from '../sidebar/+page.svelte';

  let transactions = [
    { description: "Spotify Subscription", transactionId: "#12548796", type: "Shopping", card: "1234 ****", date: "28 Jan, 12.30 AM", amount: "$2,500" },
    { description: "Freepik Sales", transactionId: "#12548796", type: "Transfer", card: "1234 ****", date: "25 Jan, 10.40 PM", amount: "$750" },
    { description: "Mobile Service", transactionId: "#12548796", type: "Service", card: "1234 ****", date: "20 Jan, 10.40 PM", amount: "$150" },
    { description: "Wilson", transactionId: "#12548796", type: "Transfer", card: "1234 ****", date: "15 Jan, 03.29 PM", amount: "$1050" },
    { description: "Emilly", transactionId: "#12548796", type: "Transfer", card: "1234 ****", date: "14 Jan, 10.40 PM", amount: "$840" },
  ];
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
        <button class="add">ADD</button>
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
</div>
