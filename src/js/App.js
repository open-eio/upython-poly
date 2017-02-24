import React, {Component} from 'react';
import Header from './components/Header';
import Fanon from './components/Fanon';
import Fanoff from './components/Fanoff';
import Lighton from './components/Lighton';
import Lightoff from './components/Lightoff';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state={
      fan: false,
      light: false
    }
    fetch(`${SERVER_ADDRESS}/pins?pin_num=2&pin_type=digital_out`, {
        mode: 'cors'
    }).then( res => res.json() ).then((res)=>{
      this.setState({fan: Boolean(res.pin_value)});
    });
    fetch(`${SERVER_ADDRESS}/pins?pin_num=13&pin_type=digital_out`, {
        mode: 'cors'
    }).then( res => res.json() ).then((res)=>{
      this.setState({light: Boolean(res.pin_value)});
    });
  }
  changeDeviceState(device, state){
    const deviceMap = {
      'fan': 2,
      'light': 13
    };
    const pin = deviceMap[device];
    fetch(`${SERVER_ADDRESS}/pins?pin_num=${pin}&pin_type=digital_out&pin_value=${Number(state)}`, {
        mode: 'cors',
        method: 'PUT'
    }).then( res => res.json() ).then((res)=>{
      this.setState({[device]: Boolean(res.pin_value)});
    });
  }
  render(){
    const fan = this.state.fan ? <Fanon/> : <Fanoff/>;
    const fanText = this.state.fan ? 'Turn Fan Off' : 'Turn Fan On'; 
    const fanButtonClass = this.state.fan ? 'button-red' : 'button-blue';
    const fanButtonAction = this.changeDeviceState.bind(this, 'fan', !this.state.fan);
    
    const light = this.state.light ? <Lighton/> : <Lightoff/>;
    const lightText = this.state.light ? 'Turn Light Off' : 'Turn Light On'; 
    const lightButtonClass = this.state.light ? 'button-red' : 'button-purple';
    const lightButtonAction = this.changeDeviceState.bind(this, 'light', !this.state.light);
    
    return (
      <div>
        <Header/>
        <div className="main">
          <div className="device">
            <h1>Fan</h1>
            {fan}
            <button onClick={fanButtonAction} className={fanButtonClass}>
              {fanText}
            </button>
          </div>
          <div className="device">
            <h1>Lights</h1>
            {light}
            <button onClick={lightButtonAction} className={lightButtonClass}>
              {lightText}
            </button>
          </div>
        </div>
      </div>
    );
  }
  
}