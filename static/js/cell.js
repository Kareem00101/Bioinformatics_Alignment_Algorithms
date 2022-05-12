var row=0
var col=0
var cell="#c" + row + col

document.querySelector('#show').addEventListener('click',()=>{
    console.log("here1", cell)
    
    document.querySelector(cell).style.visibility="hidden";
    col ++;
    cell="#c" + row + col;
    console.log(cell)
});