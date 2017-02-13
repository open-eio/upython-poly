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
    resolve: {
      extensions: ['.js'],
      alias: {
        'react': 'preact-compat',
        'react-dom': 'preact-compat',
        'react-addons-css-transition-group': 'rc-css-transition-group'
      },
    },
    module: {
        loaders: [
          {
            test: /\.js$/,
            include: [
              path.resolve('src/js'),
              path.resolve('node_modules/preact-compat/src')
            ],
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
        SERVER_ADDRESS: JSON.stringify(process.env.REMOTE_SERVER ? process.env.REMOTE_DEV_SERVER_ADDRESS : '')
      }),
    ]
};