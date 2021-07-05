import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import Board from './Board'
import { observe } from './Game'

const root = document.getElementById('root')

observe((knightPosition) =>
  ReactDOM.render(<Board knightPosition={knightPosition} />, root)
)

// ReactDOM.render(
// 	// <Square black>
// 	// 	<Knight />
// 	// </Square>,
//   <Board knightPosition={[4, 5]} />,
// 	document.getElementById("root")
// );


// ReactDOM.render(
//   <Board knightPosition={[7, 4]} />,
//   document.getElementById('root')
// )

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
