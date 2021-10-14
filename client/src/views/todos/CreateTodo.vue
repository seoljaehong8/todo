<template>
  <div>
    <input type="text" v-model.trim="title" @keyup.enter="createTodo">
    <button @click="createTodo" class='button'>추가</button>
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createTodo: function () {
      const todoItem = {
        title: this.title,
      }

      if (todoItem.title) {
        axios({
          method: 'post',
          // url: 'http://127.0.0.1:8000/todos/',
          url: `${SERVER_URL}/todos/`,
          data: todoItem,
          headers: this.setToken()
        })
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'TodoList' })
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
  }
}
</script>
<style scoped>
.button{
  margin-left:8px;
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
input{
  width:200px;
  height:20px;
}
</style>
