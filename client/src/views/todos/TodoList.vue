<template>
  <div>
    <ul class="ulbox">
      <h1>{{username}}'s todo list</h1>
      <li class="libox" v-for="(todo, idx) in todos" :key="idx">
        <span @click="updateTodoStatus(todo)" :class="{ completed: todo.completed }">{{ todo.title }}</span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <!-- <button @click="getTodos">Get Todos</button> -->
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: null,
    }
  },
  computed: {
    username() {
      return localStorage.getItem('username')
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
    getTodos: function () {
      axios({
        method: 'get',
        // url: 'http://127.0.0.1:8000/todos/',
        url: `${SERVER_URL}/todos/`,
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.todos = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      axios({
        method: 'delete',
        // url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        url: `${SERVER_URL}/todos/${todo.id}/`,
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.getTodos()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateTodoStatus: function (todo) {
      const todoItem = {
        ...todo,
        completed: !todo.completed
      }

      axios({
        method: 'put',
        // url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        url: `${SERVER_URL}/todos/${todo.id}/`,
        data: todoItem,
        headers: this.setToken(),
      })
        .then((res) => {
          console.log(res)
          todo.completed = !todo.completed
        })
      },
    },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getTodos()
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .completed {
    text-decoration: line-through;    
    color: rgb(134, 134, 134);
    font-weight: bold;
  }

  .ulbox{
    box-shadow: 0px 0px 30px 1px rgb(141, 240, 157);
    border-radius: 5px;
    width: 600px;
    margin: 0 auto;
    padding:1px 5px 10px 10px;
  }

  .libox{
    margin:10px 0;
    list-style: none;
    text-align: left;
    font-size: 1.5rem;
  }
  .libox:hover{
    cursor: pointer;
  }
</style>
