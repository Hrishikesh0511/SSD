//importing express
const express=require('express');
//import mongoose
const mongoose=require('mongoose');
//importing all the elements in env file
require('dotenv').config();
const userRoutes=require('./routes/userRoutes');
const qnaRoutes=require('./routes/qnaRoutes');
const cors = require('cors');
//express app
const app=express();
app.use(cors());
//middleware to parse JSON data
app.use(express.json());
//prints what type of method is used on what
app.use((req,res,next)=>{
    console.log(req.path,req.method);
    next();
});

//routes
app.use('/api/chatgpt/user',userRoutes);
app.use('/api/chatgpt/qna',qnaRoutes);

mongoose.connect(process.env.MONGO_URI)
.then(()=>{
    //listen to request
    app.listen(process.env.PORT,()=>{
    console.log("connected to db & listening on port",process.env.PORT);
})})
.catch((error)=>{console.log(error)});