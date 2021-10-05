<template>
  <div>
    <h1>Django로 부터 응답 받은 내용</h1>
    <span class='content'>
        {{content}}
    </span>
    
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      content: null,
    }
  },
  created: function () {
    axios({
        method: 'get',
        // url: 'http://127.0.0.1:8000/todos/',
        url: `${SERVER_URL}/`,
    })
    .then((res) => {
        this.content = res.data     
    })
    .catch((err) => {
        console.log(err)
    })
    
  }

}
</script>
<style scoped>

.content{
    font-size: 40px;
    color: rgb(36, 187, 56);
}
h1{
    margin-bottom: 50px;
}
</style>
