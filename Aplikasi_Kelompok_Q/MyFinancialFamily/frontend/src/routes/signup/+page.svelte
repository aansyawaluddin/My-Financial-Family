<script>
  import { goto } from '$app/navigation';
  import { userStore } from '../store';

  let username = "";
  let fullname = "";
  let email = "";
  let password = "";
  let gender = "";
  let role = "";
  let rememberMe = false;

  async function handleSignup() {
    const user = {
      Username: username,
      Fullname: fullname,
      Password: password,
      Gender: gender,
      Email: email.toLowerCase(),
      Role: role,
    };

    if (!username || !fullname || !email || !password || !gender || !role ) {
      alert("Silakan isi semua bidang");
      return;
    }

    if (username.length > 10) {
      alert("Username tidak boleh melebihi 10 karakter");
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:8000/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
      });

      if (response.ok) {
        const result = await response.json();
        userStore.set(result.user);
        sessionStorage.setItem('isLoggedIn', 'true');
        sessionStorage.setItem('Username', username);
        goto('home');
      } else {
        const errorData = await response.json();
        console.error("Server Response:", errorData); // Log detailed server response
        if (response.status === 400) {
          alert(errorData.detail || "Email sudah digunakan");
        } else if (response.status === 422) {
          alert("Data tidak dapat diproses: Silakan periksa data input"); 
        } else {
          alert("Terjadi kesalahan: " + response.statusText);
        }
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Terjadi kesalahan tak terduga. Silakan coba lagi nanti.");
    }
  }

</script>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">

<div class="container mt-5">
  <div class="row justify-content-center">
    <div class="col-md-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title text-center mb-4">My Financial Family</h5>
          <div class="form-group mb-3">
            <label for="username">Username</label>
            <input type="text" class="form-control" id="username" bind:value={username} maxlength="10" placeholder="Masukkan Username (maks 10)"/>
          </div>
          <div class="form-group mb-3">
            <label for="fullname">Nama Lengkap</label>
            <input type="text" class="form-control" id="fullname" bind:value={fullname} placeholder="Masukkan Nama Lengkap"/>
          </div>
          <div class="form-group mb-3">
            <label for="email">Alamat Email</label>
            <input type="email" class="form-control" id="email" bind:value={email} placeholder="Masukkan Email"/>
          </div>
          <div class="form-group mb-3">
            <label for="password">Kata Sandi</label>
            <input type="password" class="form-control" id="password" bind:value={password} placeholder="Masukkan Kata Sandi"/>
          </div>
          <div class="form-group mb-3">
            <label for="gender">Jenis Kelamin</label>
            <select class="form-select" id="gender" bind:value={gender}>
              <option value="">Pilih Jenis Kelamin</option>
              <option value="male">Laki-laki</option>
              <option value="female">Perempuan</option>
            </select>
          </div>
          <div class="form-group mb-3">
            <label for="role">Peran</label>
            <select class="form-select" id="role" bind:value={role}>
              <option value="">Pilih Peran</option>
              <option value="Mother">Ibu</option>
              <option value="Son">Anak Laki-laki</option>
              <option value="Daughter">Anak Perempuan</option>
            </select>
          </div>
          <button class="btn btn-primary w-100" on:click={handleSignup}>Daftar</button>
          <div class="text-center mt-3">
            <span>Sudah punya akun? </span><a href="/login">Masuk di sini</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
