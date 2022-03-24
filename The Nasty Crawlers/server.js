const mongoose = require("mongoose");
const path = require("path");
const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const port = 4000;

const uri = "mongodb+srv://crawleruser:crawleruser@cluster0.rj3te.mongodb.net/UserData?retryWrites=true&w=majority";
const client = mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true});

const formSchema = new mongoose.Schema({
    description: String,
    url: String
});

const Form = mongoose.model('forms', formSchema);

async function addForm(description, url) {
    let newForm = new Form({
        description: description,
        url: url
    });

    await newForm.save();
}

// const Form = main().catch(err => console.log(err));
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, '/public/Home Page.html'));
});

app.get("/complains", (req, res) => {
    res.sendFile(path.join(__dirname, '/public/Complain.html'));
});

app.post("/complains", (req, res) => {
    description = req.body.description;
    url = req.body.url;

    addForm(description, url);
    res.sendFile(path.join(__dirname, '/public/Acknowledge.html'));
});

app.listen(port, () => {
    "Server started at http://localhost:4000"
});