const Qna=require('../models/qnaModel');
const mongoose=require('mongoose');

//get all the questions
const getAllqna=async (req,res)=>{
    const qna=await Qna.find();
    if(!qna)
    {
        return res.status(404).json({error:"No Questions"});
    }
    res.status(200).json({qna});
}

//push one question to db
const pushQna= async(req,res)=>{
    try{
        const {question,answer}=req.body;
        if(!(question && answer))
        {
            res.status(400).send("Enter all inputs");
        }
        const qna=await Qna.create({question,answer});
        res.status(200).json({qna});
    }
    catch(err){
        console.log(err);
    }
}

//get one question from db
const getQna=async(req,res)=>{
    try{
        const {qid}=req.params;
        if(!mongoose.Types.ObjectId.isValid(qid))
        {
            return res.status(404).json({error:"Invalid QID"});
        }
        const qna=await Qna.findById(qid);
        if(!qna)
        {
            return res.status(404).json({error:"No such question"});
        }
        res.status(200).json({qna});
        }
        catch(error)
        {
            console.log(error);
        }
}
module.exports={
    getAllqna,
    pushQna,
    getQna
}