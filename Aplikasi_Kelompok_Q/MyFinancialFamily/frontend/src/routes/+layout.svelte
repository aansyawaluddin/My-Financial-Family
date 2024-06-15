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
