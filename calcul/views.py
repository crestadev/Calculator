from django.shortcuts import render
import math

def calculator(request):
    result = None
    error = None

    if request.method == "POST":
        try:
            num1_raw = request.POST.get("num1", "").strip()
            num2_raw = request.POST.get("num2", "").strip()
            operator = request.POST.get("operator", "+")

            num1 = float(num1_raw) if num1_raw != "" else 0.0
            num2 = float(num2_raw) if num2_raw != "" else 0.0

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    error = "Error: Division by zero"
                else:
                    result = num1 / num2

            elif operator == "sqrt":
                result = math.sqrt(num1)
            elif operator == "pow":
                result = math.pow(num1, num2)
            elif operator == "log":
                if num1 <= 0:
                    error = "Error: log requires positive number"
                else:
                    result = math.log(num1, num2 if num2 != 0 else math.e)
            elif operator == "sin":
                result = math.sin(math.radians(num1))
            elif operator == "cos":
                result = math.cos(math.radians(num1))
            elif operator == "tan":
                result = math.tan(math.radians(num1))
            else:
                error = "Unknown operator"

            if error is None:
                history = request.session.get("history", [])
                if operator in ["sqrt", "sin", "cos", "tan", "log"]:
                    history.insert(0, f"{operator}({num1}) = {result}")
                elif operator == "pow":
                    history.insert(0, f"{num1}^{num2} = {result}")
                else:
                    history.insert(0, f"{num1} {operator} {num2} = {result}")
                request.session["history"] = history[:10]
        except ValueError:
            error = "Invalid number input"
        except Exception as e:
            error = f"Error: {e}"

    history = request.session.get("history", [])
    return render(request, "calculator.html", {
        "result": result,
        "error": error,
        "history": history
    })
