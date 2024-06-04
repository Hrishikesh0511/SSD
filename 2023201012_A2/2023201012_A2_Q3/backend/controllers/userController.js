const User=require('../models/userModel');
const mongoose=require('mongoose');
const bcrypt=require('bcrypt');

//getting user info by id
const getUserinfo= async(req,res) => {
    const {userid}=req.params;
    // console.log(userid);
    if(!mongoose.Types.ObjectId.isValid(userid)) {
        return res.status(404).json({error:"Invalid UserID"});
    }
    const user= await User.findById(userid);
    if(!user) 
    {
        return res.status(404).json({error:"No Such User"})
    }
    res.status(200).json({user});
}


//logging in user
const loginUser= async(req,res) => {
    try{
        //get user input
        const {email,password}=req.body;
        if(!(email&& password))
        {
            res.status(400).json({"message":"Enter all inputs"});
        }

        const user= await User.findOne({email});
        if(user && (await bcrypt.compare(password,user.password))){
            res.status(200).json(user);
        }
        else if(user){
            res.status(400).json({"message":"Invalid Credentials"});
        }
        else
        {
            res.status(409).json({"message":"new user? try registering!!"});
        }
    }
    catch(error){
            console.log(error);
    }
}

//registering user
const registerUser= async(req,res) => {
    try{
    const{name,email,password,role}=req.body;
    if(!(email && password && name && role))
    {
        res.status(400).json({"message":"Enter all inputs"});
    }

    //check if user already exists
    
    const oldUser=await User.findOne({email});

    if(oldUser)
    {
        return res.status(409).json({"message":"User Already Exists, Please Login"});
    }

    //encrypt password
    console.log(password);
    encryptedPasswd=await bcrypt.hash(password,10);

    const user=await User.create({name,email:email.toLowerCase(),password:encryptedPasswd,role});

    res.status(201).json(user);
}
    catch(error){
        console.log(error);
    }
}


//editing user info
const editUserInfo= async (req, res) => {
    const {userid}=req.params;
    try{
    const {name,email,role}= req.body;
    if(!(email && role && name))
    {
        res.status(400).json({"message":"Enter all inputs"});
    }
    const user=await User.updateOne({_id:userid},
    {
        $set: {
            email: email,
            name: name,
            role: role
          },
          $password: { lastUpdated: true }
    })
    res.status(200).json({user});
    }
    catch (error) {
        console.log(error);
    }
}


module.exports={
    getUserinfo,
    registerUser,
    loginUser,
    editUserInfo
}