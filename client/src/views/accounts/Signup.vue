<template>
  <div>
    <div class="card">
      <h1>Signup</h1>
      <div>
        <label for="username" class="user-id">아이디</label>
        <input type="text" id="username" v-model="credentials.username">
      </div>
      <div>
        <label for="password" class="user-pw">비밀번호</label>
        <input type="password" id="password" v-model="credentials.password">
      </div>
      <div>
        <label for="passwordConfirmation" class="user-pw2">비밀번호 확인</label>
        <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
      </div>
      <button @click="signup(credentials)" class="button">회원가입</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        // url: 'http://127.0.0.1:8000/accounts/signup/',
        url: `${SERVER_URL}/accounts/signup/`,
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'Login' })
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
  width: 110px;
  display:inline-block;
  margin-bottom: 10px;
  text-align: left;
}
.user-pw{
  width: 110px;
  display:inline-block;
  text-align: left;
  margin-bottom: 10px;
}
.user-pw2{
  width: 110px;
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