import React from 'react';
import { render } from 'react-dom';

const container = document.querySelector('#target');

function renderApp() {
  const App = require('./App').default;
  const app = (<App />);
  render(app, container);
}

// Set up HMR re-rendering.
if (module.hot) {
  renderApp();
  module.hot.accept();
  module.hot.accept('./App.js', ()=>{
    console.log('rendering');
    renderApp();
  });
}

// Initial render.
renderApp();

console.log('loaded javascript');



console.log('SERVER_ADDRESS', SERVER_ADDRESS);

fetch(`${SERVER_ADDRESS}/pins?pin_num=2&pin_type=digital_out`, {
    mode: 'cors'
}).then( res => res.json() ).then((res)=>{
  console.log('pin2', res);
});