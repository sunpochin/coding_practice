import React from 'react';

export default class Task extends React.Component {
  render() {
    return this.props.task.content
  }
}
