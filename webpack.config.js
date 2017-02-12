var webpack = require('webpack');
var path = require('path');
require('dotenv').config();

module.exports = {
    entry: [
      'whatwg-fetch',
      "./src/js/entry.js" 
    ],
    target: "web",
    output: {
        path: __dirname,
        filename: "./build-temp/build.js",
    },
    module: {
        loaders: [
          {
            test: /\.js$/,
            exclude: /(node_modules|bower_components)/,
            loaders: ['babel-loader']
          },
        ]
    },
    plugins: [
      new webpack.optimize.UglifyJsPlugin({
        minimize: true,
        compress: {warnings: false},
        output: {comments: false},
        sourceMap: true
      }),
      new webpack.DefinePlugin({
        SERVER_ADDRESS: process.env.REMOTE_SERVER ? process.env.REMOTE_DEV_SERVER_ADDRESS : ''
      }),
    ]
};