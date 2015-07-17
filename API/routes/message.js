var Message = require('../models/message');

module.exports = function(app, router){
    
    router.route('/')
        // To return all stored messages
        .get(function(req, res){
            Message.find().exec(function(err, messages){
                if(err)
                    res.send({success:false, mesage:'error'});
                    
                res.json(messages);
            });
        })
        // To store a message
        .post(function(req, res){
            var message = new Message();
            message.userid = req.body.id;
            message.message = req.body.message;
            message.date = new Date();
            
            message.save(function(err){
                res.send(err);
                //res.send({success:false, message:'error saving'});
            });
        });
    
};