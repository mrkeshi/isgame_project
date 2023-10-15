const path = require('path');
const webpack = require('webpack');


module.exports = {

    mode: 'development',
    context: __dirname,
    entry: './static/assets/js/axious_main',
    output: {
        path: path.resolve('./static/assets/webpack_bundles/'),
        filename: "axious_main_bundler.js"
    },
    plugins: [

    ],
}