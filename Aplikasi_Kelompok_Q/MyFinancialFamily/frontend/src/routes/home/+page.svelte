<script>
  // @ts-nocheck
  import { onMount } from 'svelte';
  import Sidebar from '../sidebar/+page.svelte';
  import { userStore } from '../store';

  let user = {};
  let familyMembers = [];
  let desc ;

  // Subscribe to the store to get user data
  userStore.subscribe(value => {
    user = value || {};
  });

  let transactions = [];
  let categories = [];

  let currentDate = new Date().toLocaleDateString('id-ID', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  });

  async function ReadDataUser() {
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
  
  async function ReadExpenses() {
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
        categories = [];
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
        transactions = [];
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  onMount(() => {
    ReadDataUser();
    ReadExpenses();
    readTransactions();
  });
</script>

<style>
  .home {
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

  .container {
    padding: 20px;
  }
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  .header h1 {
    margin: 0;
    font-size: 24px;
  }
  .header p {
    margin: 0;
    font-size: 16px;
    color: #666;
  }
  .family-members {
    display: flex;
    gap: 40px;
    margin-bottom: 20px;
    flex-wrap: wrap;
  }
  .card {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background: #fff;
    text-align: center;
    width: calc(25% - 40px);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .card img {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    margin-bottom: 10px;
  }
  .card h3 {
    margin: 0;
    font-size: 18px;
  }
  .card p {
    margin: 5px 0;
    font-size: 14px;
    color: #666;
  }
  .main-content {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  .transactions, .expenses {
    width: 48%;
  }
  .transactions h2, .expenses h2 {
    margin: 0 0 10px;
    font-size: 20px;
  }
  .transactions-list, .expenses-list {
    border: 1px solid #ddd;
    border-radius: 10px;
    background: #fff;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  .transactions-list .tabs {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
  }
  .tabs button {
    background: none;
    border: none;
    font-size: 16px;
    cursor: pointer;
    padding: 10px 20px;
    border-bottom: 2px solid transparent;
  }
  .tabs button.active {
    border-bottom: 2px solid #000;
    font-weight: bold;
  }
  .transaction {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid #eee;
  }
  .transaction:last-child {
    border-bottom: none;
  }
  .transaction .details {
    display: flex;
    flex-direction: column;
  }
  .transaction h4 {
    margin: 0;
    font-size: 16px;
  }
  .transaction p {
    margin: 5px 0;
    font-size: 14px;
    color: #666;
  }
  .transaction .amount {
    font-size: 16px;
    font-weight: bold;
  }
  .expenses-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  .expense {
    display: flex;
    align-items: center;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background: #f9f9f9;
  }
  .expense span {
    margin-right: 10px;
    font-size: 24px;
  }
  .expense p {
    margin: 0;
    font-size: 16px;
    margin-left: 10px;
  }

  /* Media queries for responsiveness */
  @media (max-width: 1200px) {
    .card {
      width: calc(33.333% - 40px);
    }
    .transactions, .expenses {
      width: 100%;
    }
  }

  @media (max-width: 900px) {
    .card {
      width: calc(50% - 40px);
    }
    .family-members {
      gap: 20px;
    }
  }

  @media (max-width: 600px) {
    .card {
      width: 100%;
    }
    .expenses-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<div class="home">
  <div class="sidebar">
    <Sidebar active="home" />
  </div>
  <div class="content">
    <div class="container">
      <div class="header">
        <h1>Hello {user.Fullname}</h1>
        <p>{currentDate}</p>
      </div>

      <div class="family-members">
        {#each familyMembers as member}
          <div class="card">
            <img src="https://i.pinimg.com/474x/a3/f4/bc/a3f4bc0dc7d1b030b782c62d7a4781cf.jpg" alt="Profile Picture">
            <h3>{member.Fullname}</h3>
            <p>{member.Role}</p>
            <p>{member.Email}</p>
          </div>
        {/each}
      </div>

      <div class="main-content">
        <div class="transactions">
          <h2>Recent Transactions</h2>
          <div class="transactions-list">
            {#each transactions.slice(0, 5) as transaction}
              <div class="transaction">
                <div class="details">
                  <h4>{transaction.Description}</h4>
                  <p>ID Expenses : {transaction.ExpensesCategoryID}</p>
                </div>
                <div class="amount">
                  <p>Rp. {transaction.Amount}</p>
                  <p>{transaction.TransactionDate}</p>
                </div>
              </div>
            {/each}
          </div>
        </div>

        <div class="expenses">
          <h2>Expenses Breakdown</h2>
          <div class="expenses-list">
            <div class="expenses-grid">
              {#each categories as category}
                <div class="expense">
                  <img src="https://i.pinimg.com/564x/fe/99/c7/fe99c72499b9be5c1f79a33b06b3d4e1.jpg" alt={category.CategoryName} width="40" height="40">
                  <p>ID : {category.CategoryID}<br>
                    {category.CategoryName}
                  </p>
                </div>
              {/each}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
