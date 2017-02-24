import React, { Component } from 'react';
import Ribbon from './Ribbon';
import Logo from './Logo';


export default class Header extends Component {
  constructor(props) {
    super(props);
  }
  render(){
    const props = this.props;
    return (
      <div>
        <div className="header">
          <Ribbon height="4px" animate={props.loading}/>
          <div className="header-inner">
            <Logo/>
          </div>
        </div>
        <div className="header-spacer"/>
      </div>
    );
  }
}





