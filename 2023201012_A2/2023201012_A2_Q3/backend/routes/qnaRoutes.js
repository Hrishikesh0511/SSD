const express=require('express');
const{getAllqna,pushQna,getQna}=require('../controllers/qnaController');
const router=express.Router();

router.get('/',getAllqna);

router.post('/pushQna',pushQna);

router.get('/getQna/:qid',getQna);

module.exports=router;