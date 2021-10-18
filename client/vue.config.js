module.exports = {
  devServer: {
    proxy: {
      '/':{
        "target":'http://127.0.0.1:8000',
        // "target":'hello',
        "pathRewrite":{'^/':''},
        "changeOrigin":true,
        "secure":false
      }
    }
  }
}
