var pointPerValue = 30;
var canvas = document.getElementById("plotCanvas");
var plotWidth = canvas.width;
var plotHeight = canvas.height;
var xCenter = plotWidth / 2;
var yCenter = plotHeight / 2;

var lastX = 0;
var lastY = 0;

function renderPlot(rValue) {
    var context = canvas.getContext("2d");

    context.fillStyle = "#FFFFFF";
    context.fillRect(0, 0, plotWidth, plotHeight);

    var r = pointPerValue * rValue;

    //Draw
    context.beginPath();
    context.strokeStyle = "#000000";
    context.moveTo(xCenter, 0);
    context.lineTo(xCenter, plotHeight);
    context.stroke();
    context.closePath();

    context.beginPath();
    context.moveTo(0, yCenter);
    context.lineTo(plotWidth, yCenter);
    context.stroke();
    context.closePath();

    context.fillStyle = "#3399FF";

    context.beginPath();
    context.fillRect(xCenter + 1, yCenter - 1, r / 2 + 1, -r - 1);
    context.closePath();

    context.beginPath();
    context.moveTo(xCenter - 1, yCenter - 1);
    context.lineTo(xCenter - 1 - r, yCenter - 1);
    context.lineTo(xCenter - 1, yCenter - 1 - r);
    context.moveTo(xCenter - 1, yCenter - 1);
    context.fill();
    context.closePath();

    context.beginPath();
    context.arc(xCenter - 1, yCenter + 1, r / 2, Math.PI / 2, Math.PI, false);
    context.moveTo(xCenter - 1 - r / 2, yCenter + 1);
    context.lineTo(xCenter - 1, yCenter + 1);
    context.lineTo(xCenter - 1, yCenter + 1 + r / 2);
    context.fill();
    context.closePath();
}

function drawPoint(x, y, hit) {
    var context = canvas.getContext("2d");
    context.beginPath();
    if (hit)
        context.fillStyle = "#00FF00";
    else
        context.fillStyle = "#FF0000";
    y = -y;
    context.arc(x * pointPerValue + xCenter - 2, y * pointPerValue + yCenter - 2, 4, 0, 2 * Math.PI);
    context.fill();
    console.log(hit);
}

canvas.addEventListener('click', function (event) {
    var x = event.pageX - canvas.offsetLeft - xCenter,
        y = -event.pageY + canvas.offsetTop + yCenter;
    sendPoint(x / pointPerValue, y / pointPerValue);
    // lastX = x / pointPerValue;
    // lastY = -(y / pointPerValue);
}, false);