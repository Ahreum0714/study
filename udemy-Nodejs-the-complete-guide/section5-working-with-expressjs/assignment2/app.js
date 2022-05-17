const express = require("express");

const app = express();

app.use("/", (req, res, next) => {
  console.log("always runs");
  next();
});

app.use("/users", (req, res, next) => {
  console.log("url: /users");
  res.send("<h1>url: /users</h1>");
});

app.use("/", (req, res, next) => {
  console.log("url: /");
  res.send("<h1>Hello from Express!</h1>");
});

app.listen(3000);
