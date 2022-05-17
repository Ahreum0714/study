const path = require("path");

const express = require("express");

const router = express.Router();

router.get("/", (req, res, next) => {
  res.sendFile(path.join(__dirname, "../", "views", "shop.html")); // __dirname: 현재 프로젝트 폴더의 absolute path --> routes폴더
});

module.exports = router;
