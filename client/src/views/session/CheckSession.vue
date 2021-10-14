<template>
    <div>
        <h1>checkSession</h1>
    </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CheckSession',
  data: function () {
    return {
      sessionId: '',
      sessionValue: '',
    }
  },
  created: function() {
      axios({
          method:'get',
          url:`${SERVER_URL}/accounts/checkSession/`
      })
      .then(res=>{
          console.log(res.data)
          this.sessionId = res.data.session_id
          this.sessionValue = res.data.test
      })
      .catch(err=>{
          console.log(err)
      })
  }
}
</script>