from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import math

@csrf_exempt
def calculator(request):
    result = None
    error = None

    if "history" not in request.session:
        request.session["history"] = []

    if request.method == "POST" and "clear_history" in request.POST:
        request.session["history"] = []
        request.session.modified = True
        return render(request, "calc/calculator.html", {"history": []})

    if request.method == "POST" and "clear_history" not in request.POST:
        try:
            num1 = float(request.POST.get("num1", 0))
            num2 = float(request.POST.get("num2", 0))
            operator = request.POST.get("operator")

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2 if num2 != 0 else "Division by zero!"
            elif operator == "sqrt":
                result = math.sqrt(num1)
            elif operator == "pow":
                result = math.pow(num1, num2)
            elif operator == "log":
                result = math.log(num1, num2) if num1 > 0 and num2 > 0 else "Invalid log input!"
            elif operator == "sin":
                result = math.sin(math.radians(num1))
            elif operator == "cos":
                result = math.cos(math.radians(num1))
            elif operator == "tan":
                result = math.tan(math.radians(num1))
            else:
                error = "Invalid operator"

            if not error and result is not None:
                history_entry = f"{num1} {operator} {num2} = {result}"
                request.session["history"].append(history_entry)
                request.session["history"] = request.session["history"][-5:]  # keep last 5
                request.session.modified = True

        except Exception as e:
            error = str(e)

    return render(request, "calc/calculator.html", {
        "result": result,
        "error": error,
        "history": request.session.get("history", [])
    })
