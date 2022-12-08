import React from 'react';


class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state = { date: new Date() };  // declare a new state object. state is a special property and only accessible locally.
    }

    // lifecycle method, is called after the component output has been rendered to the DOM
    componentDidMount() {
        this.timerID = setInterval(
            () => this.tick(),  // arrow function, so that 'this' is bound to the class
            1000
        );
    }

    // lifecycle method, is called when the component is removed from the DOM
    componentWillUnmount() {
        clearInterval(this.timerID);
    }

    tick() {
        this.setState({  // always use setState() to update the state (except in the constructor)
            date: new Date()
        });
    }

    render() {
        return (
            <div>
                <h2>It is {this.state.date.toLocaleTimeString()}</h2>
            </div>
        );
    }
}

export default Clock;
