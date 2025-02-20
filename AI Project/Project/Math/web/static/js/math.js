document.getElementById("calculate-button").addEventListener("click", () => {
    const number1 = parseFloat(document.getElementById("number1").value);
    const number2 = parseFloat(document.getElementById("number2").value);
    const operation = document.getElementById("operation").value;
    let result;

    if (isNaN(number1) || isNaN(number2)) {
        alert("Please enter valid numbers!");
        return;
    }

    switch (operation) {
        case "add":
            result = number1 + number2;
            break;
        case "subtract":
            result = number1 - number2;
            break;
        case "multiply":
            result = number1 * number2;
            break;
        case "divide":
            if (number2 === 0) {
                alert("Cannot divide by zero!");
                return;
            }
            result = number1 / number2;
            break;
        default:
            alert("Please select a valid operation!");
            return;
    }

    document.getElementById("result").innerText = result;
});
