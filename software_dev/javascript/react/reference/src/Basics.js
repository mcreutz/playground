import React from 'react';


// component as function
function WelcomeFunc(props) {
  return <h1>Hello, I am a {props.name}</h1>;
  // components are never allowed to modify their own props
}

// component as class
class WelcomeCls extends React.Component {
  render() {
    return <h1>Hello, I am a {this.props.name}</h1>;
  }
}

// hooks ?
// setInterval(FunctionName, 1000);

function Basics() {
  return (
    <div className="Basics">
      <WelcomeFunc name="function" />
      <WelcomeCls name="class" />
      <a href='/clock'>Clock</a>
    </div>
  );
}

export default Basics;
