var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var MessageSchema = new Schema({
    userid: { type: 'String', unique: false },
    message: { type: 'String', unique: false },
    date: String
});

module.exports = mongoose.model('Message', MessageSchema) ;
