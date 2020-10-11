var express = require('express');
var mongoose = require('mongoose');
var Promise = require('promise');
var axios = require('axios').default;
require('dotenv').config();
var bodyParser = require('body-parser');
var cors = require('cors');
var path = require('path');

//https://stackoverflow.com/questions/59925931/get-request-to-port-81-using-axios-or-even-js-native-fetch
//Might need to use this to talk to another server hosted on same computer
//Can also wrap the axios calls to make it look prettier http://zetcode.com/javascript/axios/

const router = express.Router();
var app = express();
app.use(cors())
app.use(express.urlencoded({ extended: true })); 
app.use(express.json());
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }));


var mongodb = process.env.DB
const port = 3000;

mongoose.connect(mongodb, {useNewUrlParser: true, useUnifiedTopology: true});

var db = mongoose.connection;

db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', function() {
    // we're connected!
    console.log("we be connected");
});

var HashCountSchema = new mongoose.Schema({
    hashtag: String,
    count: Number
})

var Hashtag = mongoose.model("Hashtag", HashCountSchema)

//initial page
router.get('/', (req, res) => {
    res.sendFile(path.join(__dirname+'/public/index.html'));
}); 

//process hashtags
router.get('/test', (req,res) =>{
    hashtags = req.body.hashtags

    //Use axios to send hashtag to python scraper
    axios.get('http://127.0.0.1:5000/', { 
        params: {data: JSON.stringify(hashtags)},
        headers: {'Content-Type': 'application/json'}
    })
    .then( (flask_res) => {
        res.send(flask_res.data)
        //store data into MongoDB
        data = flask_res.data["hashtag"]
        for (var key in data){
            var hash = key
            var num = data[key]
            var obj = {
                hashtag: hash,
                count: num
            }
            
            var dataTest = new Hashtag(obj)
            dataTest.save()
        
        }
    })
    .catch((err) => {
        console.log(err)
        res.sendStatus(404);
    });
});

app.use('/',router)

app.listen(port, () =>  {
    console.log("hi")
});