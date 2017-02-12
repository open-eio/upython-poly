console.log('loaded javascript');

console.log('SERVER_ADDRESS', SERVER_ADDRESS);

fetch('http://swapi.co/api/films', {
    mode: 'cors'
}).then( res => res.json() ).then((res)=>{
  console.log('star wars films from swapi', res);
});