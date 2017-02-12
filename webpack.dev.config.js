var webpack = require('webpack');
var path = require('path');
require('dotenv').config();

module.exports = {
    entry: [
      "webpack-dev-server/client?http://localhost:5000",
      // "webpack/hot/only-dev-server",
      'whatwg-fetch',
      "./src/js/entry.js" 
    ],
    contentBase: "localhost:3000",
    historyApiFallback: true,
    output: {
        path: __dirname,
        filename: "./build.js",
        publicPath: "http://localhost:5000/"
    },
    target: "web",
    module: {
        loaders: [
          {
            test: /\.js$/,
            exclude: /(node_modules|bower_components)/,
            loaders: [
              // 'react-hot', 
              'babel-loader'
            ]
          },
        ]
    },
    devtool: 'source-map',
    plugins: [
      new webpack.DefinePlugin({
        SERVER_ADDRESS: JSON.stringify(process.env.REMOTE_SERVER ? process.env.REMOTE_DEV_SERVER_ADDRESS : process.env.LOCAL_DEV_SERVER_ADDRESS),
      }),
    ]
};