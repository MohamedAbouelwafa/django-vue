const { defineConfig } = require('@vue/cli-service')
const path = require('path');

module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: '/static/vue/dist/', // STATIC_URL + path/to/build
  outputDir: path.resolve(__dirname, '../static/vue/dist/'), // Write o/p to a directory in STATICFILES_DIRS
  filenameHashing: false, // Django will hash file names, not webpack
  runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
  devServer: {
    devMiddleware: {
      writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
    }
  },
})
