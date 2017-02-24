import React, { Component, PropTypes } from 'react';
import classNames from 'classnames';


export default class Ribbon extends Component {
  constructor(props) {
    super(props);
  }
  render(){
    const props = this.props;
    const animate = props.animate;
    const colors = ['yellow', 'red', 'purple', 'blue', 'navy'];
    return (
      <div className="ribbon" style={{height: props.height}}>
        {
          colors.map((color, index) => {
            const classes = classNames(`ribbon-${color}`, { [`ribbon-${color}-animate`]: animate });
            return <div key={index} className={classes}/>;
          })
        }
      </div>
    );
  }
}