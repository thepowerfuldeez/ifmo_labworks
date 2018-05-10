function check(_form) {
    var y = _form.Y.value;
    regexp = /^-?\d*\d(\.\d+)?$/;
    var flag = true;
    y = y.trim();

    flag = flag && regexp.test(y);
    var yi = parseInt(y);
    if(yi < -5 || yi > 5)
        flag = false;
    if (!flag) {
        document.querySelector("input[name='Y']").style.borderColor = "red";
    } else {
        var ytext = document.querySelector("input[name='Y']").style.borderColor = "initial";
        var nodeFrame = document.querySelector("iframe[name='resultsFrame']");
        nodeFrame.hidden = "";
    }
    return flag;
}

