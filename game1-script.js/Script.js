var lastPaintTime = 0;
const SNAKE_SPEED = 3;

const snakeBody =[
    {x : 10 , y :10}
];
function paint(currentTime){
    var TimeSeconds = (currentTime - lastPaintTime)/100;
    requestAnimationFrame(paint);
    if(TimeSeconds <1/SNAKE_SPEED) return;
    lastPaintTime = currentTime;

    update();
    draw();
}
window.requestAnimationFrame(paint);

const gameBoard = document.querySelector(".game-border");

function draw(){
    drawSnake();
}

function drawSnake(){
    snakeBody.forEach(segment =>{
        var snakeElement =document.createElement("div");
        snakeElement.style.gridColumntart = segment.x;
        snakeElement.style.gridRowStart = segment.y;
        snakeElement.classList.add("snake");
        gameBoard.appendChild(snakeElement);
    })
}