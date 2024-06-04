const express=require('express');
const{getUserinfo,registerUser,loginUser,editUserInfo}=require('../controllers/userController');
const router=express.Router();

//to get user info to front end
router.get('/:userid', getUserinfo);
//to post register info to db
router.post('/register', registerUser);
//to post login info to db
router.post('/login',loginUser);
//edit user info
router.post('/edit/:userid',editUserInfo);

module.exports = router;
