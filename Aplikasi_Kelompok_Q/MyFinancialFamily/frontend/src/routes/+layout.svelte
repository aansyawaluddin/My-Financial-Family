<script>
	import './styles.css';
	import 'bootstrap/dist/css/bootstrap.min.css';
	
	
	//gunanya ini kode agar ketika meng akses"http://sessionhost:5173/" akan langsung terarahkan ke "http://sessionhost:5173//login"
	import { onMount } from 'svelte';
  	import { goto } from '$app/navigation';

  	onMount(() => {
		let isLoggedIn = sessionStorage.getItem("isLoggedIn")
    
		if(isLoggedIn == 'true'){
			if(window.location.pathname === '/login'){
			sessionStorage.setItem('isLoggedIn', "false"); // Menyimpan status login di sessionStorage
			}
			if(window.location.pathname === '/sidebar'){
				//tidak bisa mengakses sidebar akan kembali ke halaman sebelumny
				history.back()

			}
		}else{
			if(window.location.pathname === '/signup'){
				
			}else{
				goto('/login')
			}
		}

		if (window.location.pathname === '/' ) {
			sessionStorage.setItem('isLoggedIn', "false"); // Menyimpan status login di sessionStorage
			goto('/login');
		}


    // Event listener untuk menangani peristiwa saat tombol back ditekan
		const handlePopState = () => {
			sessionStorage.removeItem('isLoggedIn'); // Hapus status login dari sessionStorage
			sessionStorage.removeItem('user'); // Hapus status login dari sessionStorage
			sessionStorage.removeItem('UserID'); // Hapus status login dari sessionStorage
			goto('login'); // Redirect pengguna ke halaman login setelah logout
		};
	
		window.addEventListener('popstate', handlePopState); // Tambahkan event listener untuk tombol back
	
		// Membersihkan event listener saat komponen dihancurkan atau tidak lagi digunakan
		return () => {
		window.removeEventListener('popstate', handlePopState); // Hapus event listener saat komponen di-unmount
		};
  });
</script>
<svelte:head>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" integrity="sha384-k6RqeWeci5ZR/Lv4MR0sA0FfDOMQEDdOs7A4PIyjNy3JZjKVyj5S9/ub+OvRl3w4" crossorigin="anonymous">
</svelte:head>

<div class="app">
	<main>
		<slot />
	</main>
	<footer>
	</footer>
</div>

