import React from 'react';


export function Form() {
    function handleSubmit(e) {
        e.preventDefault();
        console.log('You clicked submit.');
    }

    return (
        <form onSubmit={handleSubmit}>
            <button type="submit">Submit</button>
        </form>
    );
}


export class Toggle extends React.Component {
    constructor(props) {
        super(props);
        this.state = { isToggleOn: true };

        // This binding is necessary to make `this` work in the callback, as it was not referenced as an arrow function
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {
        this.setState(prevState => ({
            isToggleOn: !prevState.isToggleOn
        }));
    }

    render() {
        return (
            <button onClick={this.handleClick}>
                {this.state.isToggleOn ? 'ON' : 'OFF'}
            </button>
        );  // `handleClick` needs binding, as is not an arrow function
    }
}


export class WithParam extends React.Component {
    constructor(props) {
        super(props);
        this.state = { my_key: 'hello' };
    }

    handleClick(my_prop) {
        this.setState(() => ({
            my_key: my_prop
        }));
    }

    render() {
        return (
            <button onClick={this.handleClick.bind(this, 'world')}>
                {this.state.my_key}
            </button>
        );
    }
}