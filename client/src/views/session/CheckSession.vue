<template>
    <div>
        <h1>cache : {{cacheText}}</h1>

    </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CheckSession',
  data: function () {
    return {
      cacheText: '',
    }
  },
  created: function() {
      axios({
          method:'get',
          url:`${SERVER_URL}/accounts/checkSession/`
      })
      .then(res=>{
          console.log(res.data)
          this.cacheText = res.data.cache
      })
      .catch(err=>{
          console.log(err)
      })
  }
}
</script>