function calculate() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operation = document.getElementById('operation').value;
    let result = '';

    if (isNaN(num1) || isNaN(num2)) {
        result = "Enter valid numbers";
    } else {
        if (operation === '+') {
            result = num1 + num2;
        } else if (operation === '-') {
            result = num1 - num2;
        } else if (operation === '*') {
            result = num1 * num2;
        } else if (operation === '/') {
            if (num2 === 0) {
                result = "Cannot divide number by 0";
            } else {
                result = num1 / num2;
            }
        }
    }
    document.getElementById('result').innerHTML = "Result: " + result;
}

function calculate2() {
    const num3 = parseFloat(document.getElementById('num3').value);
    const num4 = parseFloat(document.getElementById('num4').value);
    const operation2 = document.getElementById('operation2').value;
    let result2 = '';

    if (isNaN(num3) || isNaN(num4)) {
        result2 = "Enter valid numbers";
    } else {
        if (operation2 === '+') {
            result2 = num3 + num4;
        } else if (operation2 === '-') {
            result2 = num3 - num4;
        } else if (operation2 === '*') {
            result2 = num3 * num4;
        } else if (operation2 === '/') {
            if (num4 === 0) {
                result2 = "Cannot divide number by 0";
            } else {
                result2 = num3 / num4;
            }
        }
    }
    document.getElementById('result2').innerHTML = "Result: " + result2;
}

function IncreaseValue(inputId) {
    const input = document.getElementById(inputId);
    input.value = parseFloat(input.value) + 1;
}

function DecreaseValue(inputId) {
    const input = document.getElementById(inputId);
    input.value = parseFloat(input.value) - 1;
}

function calculate3() {
    const num5 = parseFloat(document.getElementById('num5').value);
    const num6 = parseFloat(document.getElementById('num6').value);
    const operation3 = document.querySelector('input[name="operation3"]:checked').value;
    let result3 = '';

    if (isNaN(num5) || isNaN(num6)) {
        result3 = "Enter valid numbers";
    } else {
        if (operation3 === '+') {
            result3 = num5 + num6;
        } else if (operation3 === '-') {
            result3 = num5 - num6;
        } else if (operation3 === '*') {
            result3 = num5 * num6;
        } else if (operation3 === '/') {
            if (num6 === 0) {
                result3 = "Cannot divide number by 0";
            } else {
                result3 = num5 / num6;
            }
        }
    }
    document.getElementById('result3').innerHTML = "Result: " + result3;
}