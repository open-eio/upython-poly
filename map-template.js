var fs = require('fs');

var files = {
  "js": "./build-temp/build.js",
  "css": "./build-temp/build.css"
};

if (!fs.existsSync("./build-temp")){
    fs.mkdirSync("./build-temp");
}

console.log(process.env.NODE_ENV);

var map = {
  PRODUCTION: process.env.NODE_ENV === 'production',
  DEVELOPMENT: process.env.NODE_ENV === 'development'
};

var promises = Object.keys(files).map(function(key){
  return new Promise(function(resolve, reject){
    fs.readFile(files[key], "utf-8", function(err, data) {
      if (data){
        map[key] = data.toString();
      }else{
        map[key] = '';
      }
      resolve();
    });
  });
});

Promise.all(promises).then(function(){
  var fs = require('fs');
  fs.writeFile("./build-temp/template-map.json", JSON.stringify(map), function(err) {
    if(err) {
        return console.log(err);
    }else{
      console.log("✅  Wrote template map");
    }
  }); 
});



