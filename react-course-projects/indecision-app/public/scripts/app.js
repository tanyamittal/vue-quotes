"use strict";

console.log('App.js is running!');

var template = React.createElement(
  "p",
  null,
  "This is our JSX! and its awesome"
);
var appRoot = document.getElementById("app");

ReactDOM.render(template, appRoot);
