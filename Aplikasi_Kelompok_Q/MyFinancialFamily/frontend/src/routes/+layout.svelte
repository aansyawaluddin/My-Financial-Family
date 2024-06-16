<script>
	import Header from './Header.svelte';
	import './styles.css';

	//gunanya ini kode agar ketika meng akses"http://localhost:5173/" akan langsung terarahkan ke "http://localhost:5173//login"
	import { onMount } from 'svelte';
  	import { goto } from '$app/navigation';

  	onMount(() => {
    if (window.location.pathname === '/') {
      goto('/login');
    }
	let isLoggedIn = localStorage.getItem("isLoggedIn")
    
	if(isLoggedIn == 'true'){
		if(window.location.pathname === '/login'){
			localStorage.setItem('isLoggedIn', "false"); // Menyimpan status login di localStorage
		}
	}else{
		goto('/login');
		
	}

    // Event listener untuk menangani peristiwa saat tombol back ditekan
	const handlePopState = () => {
		localStorage.removeItem('isLoggedIn'); // Hapus status login dari localStorage
    	localStorage.removeItem('user'); // Hapus status login dari localStorage
    	localStorage.removeItem('UserID'); // Hapus status login dari localStorage
    	goto('login'); // Redirect pengguna ke halaman login setelah logout
    };
  
    window.addEventListener('popstate', handlePopState); // Tambahkan event listener untuk tombol back
  
    // Membersihkan event listener saat komponen dihancurkan atau tidak lagi digunakan
    return () => {
      window.removeEventListener('popstate', handlePopState); // Hapus event listener saat komponen di-unmount
    };
  });
</script>

<div class="app">


	<main>
		<slot />
	</main>

	<footer>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		width: 100%;
		max-width: 64rem;
		margin: 0;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 0px 0;
		}
	}
</style>
