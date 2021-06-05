//jshint esversion:6
// models/Book.js

const mongoose = require('mongoose');

const BookSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true
  },
  content: {
    type: String,
    required: true
  },
  // published_date: {
  //   type: Date
  // },
  // publisher: {
  //   type: String
  // },
  // updated_date: {
  //   type: Date,
  //   default: Date.now
  // }
});

module.exports = Book = mongoose.model('book', BookSchema);
