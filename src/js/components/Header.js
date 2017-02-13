import React, { Component } from 'react';
import Ribbon from './Ribbon';
import Logo from './Logo';
import ReactCSSTransitionGroup from 'react-addons-css-transition-group';
import InlineSVG from 'svg-inline-react';


export default class Header extends Component {
  constructor(props) {
    super(props);
  }
  render(){
    const props = this.props;
    return (
      <div>
        <div className="header">
          <Error error={props.error} dismissError={props.dismissError}/>
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

class Error extends Component {
  constructor(props) {
    super(props);
  }
  render(){
    const props = this.props;
    const message = props.error ?
        <div className="header-error" key="errorMessage">
          <div className="header-error-text">{props.error}</div>
          <div className="header-error-dismiss icon-close" onClick={props.dismissError}/>
        </div> : <span key="noErrorMessage"/>;
    return(
        <ReactCSSTransitionGroup
          transitionName="header-error-transition"
          transitionEnterTimeout={500}
          transitionLeaveTimeout={500}
          >
          {message}
        </ReactCSSTransitionGroup>
    );
  }
}



