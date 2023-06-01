// // console.log("Hello External.!!");
// // Basics of Programming in JavaScript
// /////////////////////////////////////////////
// // comments in JS 
// // shortcut : 
// // ctrl(Hold) + / 
// // Single Line Comment   syntax :   '//'
// // Multi Line Comment    syntax :   '/*' and '*/'
// // Multi 
// // line 
// // comments 

// //////////////////////////////////////////
// // ● Hello world program
// // console.log("Hello World JS.!!");
// /////////////////////////////////////
// // ● Declare variable using var
// // ● Null, undefined, BigInt, typeof
// // var , let ,const 

// // fname = "zafar" 
// // age  = 10;
// // Your Name is Zafar.and your age is 10;

// //number,string,boolean,object,null,undefined
// var fName = "Zafar";
// var number = 12.3456;
// var bool = true; //false
// var Array1 = [1,245,12];
// var Values = null;
// var Values2 = undefined;
// console.log(typeof(fName));
// console.log(fName);
// console.log(typeof number);
// console.log(number);
// console.log(typeof bool);
// console.log(bool);
// console.log(typeof Array1);
// console.log(Array1);
// console.log(typeof Values);
// console.log(Values);
// console.log(typeof Values2);
// console.log(Values2);
// var number1 = 12345678901234567890n; //bigInt
// console.log(typeof number1);
// console.log(number1);
// ////////////////////////////////////
// // ● More about variable
// // 1) don't start with Number 
// // var 1number = 12; //invalid
// // console.log(1number);

// // 2) don't use Special Char 
// // var number@ = 12; //invalid

// // Use can Use only 
// var _number = 12; //valid
// console.log(_number);
// var $number = 13;
// console.log($number);

///////////////////////////////////////////
// ● Let
// let fname = "My Name is Zafar.";
// console.log(fname);
// // ● Const

// const Name = "My Name is Zafar.";
// console.log(Name);

// var vs let vs const 
// 1) var  (you can assign Value multi time) (multiple time Declare)
var Value1 = 12;
Value1 = 1001;

var Value1 = 2001;

console.log(Value1);

// 2) let      (you can assign Value Multi time)  (only once time Declare)
// let Value2 = 13;
// Value2 = 1002;
// let Value2 = 2002;
// console.log(Value2);

// // 3) const  (you can assign Value once time)(only once time Declare)
const Value3 = 3.14;
Value3=1003;
// const Value3 = 3003;
console.log(Value3);