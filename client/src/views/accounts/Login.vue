<template>
  <div>
    <div class='card'>
      <h1>Login</h1>
      <div>
        <label for="username" class="user-id">아이디</label>
        <input type="text" id="username" v-model="credentials.username">
      </div>
      <div>
        <label for="password" class="user-pw">비밀번호</label>
        <input type="password" id="password" v-model="credentials.password" @keydown.enter="login">
      </div>
      <button @click="login" class="button">로그인</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        // url: 'http://127.0.0.1:8080/api/accounts/api-token-auth/',
        url: `${SERVER_URL}/accounts/api-token-auth/`,
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          localStorage.setItem('username', this.credentials.username)
          sessionStorage.setItem('session','this is session storage item')

          this.$emit('login')
          this.$router.push({ name: 'TodoList' })

        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
<style scoped>
.card{
  margin:0 auto;
  position: relative;
  display:inline-block;
}
.user-id{
  width: 80px;
  display:inline-block;
  margin-bottom: 10px;
  text-align: left;
}
.user-pw{
  width: 80px;
  display:inline-block;
  text-align: left;
}
.button{
  position: absolute;
  margin-top:20px;
  right: 0;
  font-size:16px;
  background-color: rgb(64, 167, 43);
  padding: 5px 10px;
  border-radius: 5px;
  border-style: none;
  color:white;
  cursor: pointer;
}
.button:hover{
  background-color: rgb(98, 206, 77);
}
</style>