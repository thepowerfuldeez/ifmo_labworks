var timeout;


function validate(_form) {

    var fail = false;
    var Y = _form.Y.value;
    var R = _form.R.value;
    var X = $("#X_s").text();
    if (Y < -5 || Y > 5 || isNaN(Y) || Y === "" || Y.length > 10) {
        fail = "Y value is incorrect ! \n";
    }
    else if (isNaN(R) || R === "" || R.length > 10) {
        fail = "choose R \n";
    }

    if (fail) {
        alert(fail);
        return false;
    }
    else {
        doRequest(Number(X), Number(Y), R);
        return true;
    }
}

function clearTable() {
    $.ajax({
        type: "post",
        url: "control",
        data: {
            cx: "-999.99",
            cy: "-999.99",
            cr: "-999.99"
        }
    });
    $('#tablehead').nextAll().remove();
}


function doRequest(x, y, r) {
    x = x.toFixed(2);
    y = y.toFixed(2);

    $.ajax({
        type: "post",
        url: "control",
        data: {
            cx: x,
            cy: y,
            cr: r
        },
        success: onAjaxSuccess
    });

    function onAjaxSuccess(result) {
        //new_data = JSON.parse(data);
        var str = "<tr><td>" + x + "</td><td>" + y + "</td><td>" + r + "</td><td>" + (result === '1' ? 'Yes' : 'No') +
            "</td></tr>";
        //$("#points").append(str);
        $(str).insertAfter("#tablehead");

        //$("#points").html(str + $("#points").html());
        var cx = (130 / r) * x + 150;
        var cy = 150 - (130 / r) * y;
        if (result === "1")
            drawPoint(cx, cy, true);
        else
            drawPoint(cx, cy, false);
    }
}

//--------------------------------------------------------------------

function drawCanvas(id, r) {
    var canvas = document.getElementById(id),
        context = canvas.getContext("2d");

    //очистка
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = "#3d7bb0";

    //прямоугольник
    context.fillRect(150, 150, 65, 130);

    //треугольник
    context.beginPath();
    context.moveTo(20, 150);
    context.lineTo(150, 280);
    context.lineTo(150, 150);
    context.fill();

    // сектор
    context.beginPath();
    context.moveTo(150, 150);
    context.arc(150, 150, 65, 1.5 * Math.PI, Math.PI);
    context.fill();

    context.strokeStyle = "black";
    context.fillStyle = "black";
    //отрисовка осей
    context.beginPath();
    context.font = "10px Verdana";
    context.moveTo(150, 0);
    context.lineTo(150, 300);
    context.moveTo(150, 0);
    context.lineTo(145, 15);
    context.moveTo(150, 0);
    context.lineTo(155, 15);
    context.fillText("Y", 160, 10);
    context.moveTo(0, 150);
    context.lineTo(300, 150);
    context.moveTo(300, 150);
    context.lineTo(285, 145);
    context.moveTo(300, 150);
    context.lineTo(285, 155);
    context.fillText("X", 290, 135);

    // деления Y по 65 пикселей
    context.moveTo(145, 20);
    context.lineTo(155, 20);
    context.fillText(r, 160, 20);
    context.moveTo(145, 85);
    context.lineTo(155, 85);
    context.fillText((r / 2), 160, 78);
    context.moveTo(145, 215);
    context.lineTo(155, 215);
    context.fillText(-(r / 2), 160, 215);
    context.moveTo(145, 280);
    context.lineTo(155, 280);
    context.fillText(-r, 160, 280);
    // деления X по 65 пикселей
    context.moveTo(20, 145);
    context.lineTo(20, 155);
    context.fillText(-r, 20, 170);
    context.moveTo(85, 145);
    context.lineTo(85, 155);
    context.fillText(-(r / 2), 70, 170);
    context.moveTo(215, 145);
    context.lineTo(215, 155);
    context.fillText((r / 2), 215, 170);
    context.moveTo(280, 145);
    context.lineTo(280, 155);
    context.fillText(r, 280, 170);

    context.closePath();
    context.strokeStyle = "black";
    context.fillStyle = "black";
    context.stroke();
}


function clickCanvas(event) {
    var elem = document.getElementById('canvas');
    var br = elem.getBoundingClientRect();
    var left = br.left;
    var top = br.top;
    var x = event.clientX - left;
    var y = event.clientY - top;
    var R = document.getElementById('form').R.value;
    if (isNaN(R) || R === "" || R.length > 10) {
        alert("choose R");
        return;
    }
    x = R * (x - 150) / 130;
    y = R * (150 - y) / 130;

    doRequest(x, y, R);
}

function isArea(X, Y, R) {
    var x = R * (X - 150) / 130;
    var y = R * (150 - Y) / 130;
    if (x <= 0 && y >= 0 && x * x + y * y <= R * R) {
        return true;
    }
    if (x >= 0 && y >= 0 && y <= (R - x) / 2) {
        return true;
    }
    if (x >= 0 && y <= 0 && x <= R && y >= (-1) * R) {
        return true;
    }
    return false;
}

function drawPoint(x, y, isArea) {
    var canvas = document.getElementById('canvas'),
        context = canvas.getContext("2d");

    context.beginPath();
    context.arc(x, y, 2, 2 * Math.PI, 0);
    context.closePath();

    if (isArea === true) {
        context.strokeStyle = "#00ff00";
        context.fillStyle = "#00ff00";
    } else {
        context.strokeStyle = "#ff0000";
        context.fillStyle = "#ff0000";
    }
    context.fill();
    context.stroke();
}
