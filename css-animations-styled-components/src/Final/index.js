import React from 'react';

import CoolBox from '../CoolBox';

export class Final extends React.Component {
  constructor(props) {
    super(props);
    this.state = { isCool: false }
  }

  toggleCoolness = () => {
    this.setState({ isCool: !this.state.isCool })
  }

  render() {
    const { isCool } = this.state;
    return (
      <div>
        <button onClick={this.toggleCoolness}>Click Me</button>
        {isCool ? (
          <CoolBox />
        ) : (
          <div></div>
        )}
      </div>
    );
  }
}

export default Final;
