import React from 'react';
import styled from 'styled-components';
import { Draggable } from 'react-beautiful-dnd';

const Container = styled.div`
  border: 1px solid lightgrey;
  border-radius: 2px;
  padding: 8px;
  margin-bottom: 8px;
  background-color: green;
`;

export default class Task extends React.Component {
  render() {
    return (
    <Draggable draggableId={this.props.task.id} index={this.props.index}>
      {provided => (
        <Container
          ref={provided.innerRef}
          {...provided.draggableProps}
          {...provided.dragHandleProps}
        >
          {this.props.task.content}
        </Container>
      )}
    </Draggable>
    );
  }
}

// import React from "react";
// import styled from "styled-components";
// import { Draggable } from "react-beautiful-dnd";

// const Container = styled.div`
// 	border: 1px solid lightgrey;
// 	border-radius: 2px;
// 	padding: 8px;
// 	margin-bottom: 8px;
// `;

// export default class Task extends React.Component {
// 	render() {
// 		return (
// 			<Draggable draggableId={this.props.task.id} index={this.props.index}>
// 				{provided => (
// 					<Container
// 						{...provided.draggableProps}
// 						{...provided.draggableProps}
// 					>
// 						{this.props.task.content}
// 					</Container>
// 				)}
// 			</Draggable>
// 		);
// 	}
// }

// // export default class Task extends React.Component {
// // 	render() {
// // 		<Draggable draggableId={this.props.task.id} index={this.props.index}>
// // 			return <Container>{this.props.task.content}</Container>;
// // 		</Draggable>;
// // 	}
// // }
