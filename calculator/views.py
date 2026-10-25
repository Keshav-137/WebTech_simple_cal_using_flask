from decimal import Decimal, DecimalException, InvalidOperation

from django.shortcuts import render


OPERATIONS = {
    "add": ("+", lambda first, second: first + second),
    "subtract": ("−", lambda first, second: first - second),
    "multiply": ("×", lambda first, second: first * second),
    "divide": ("÷", lambda first, second: first / second),
}


def _format_result(value):
    return format(value.normalize(), "f")


def calculator(request):
    context = {
        "first_number": "",
        "second_number": "",
        "selected_operation": "add",
        "result": None,
        "error": None,
    }

    if request.method == "POST":
        first_value = request.POST.get("first_number", "").strip()
        second_value = request.POST.get("second_number", "").strip()
        operation = request.POST.get("operation", "")
        context.update(
            first_number=first_value,
            second_number=second_value,
            selected_operation=operation if operation in OPERATIONS else "add",
        )

        if not first_value or not second_value:
            context["error"] = "Enter both numbers."
        elif operation not in OPERATIONS:
            context["error"] = "Choose a valid operation."
        else:
            try:
                first = Decimal(first_value)
                second = Decimal(second_value)
                if not first.is_finite() or not second.is_finite():
                    raise InvalidOperation
                if operation == "divide" and second == 0:
                    context["error"] = "You cannot divide by zero."
                else:
                    result = OPERATIONS[operation][1](first, second)
                    context["result"] = _format_result(result)
            except (InvalidOperation, ValueError, DecimalException):
                context["error"] = "Enter valid finite numbers."

    return render(request, "calculator/index.html", context)
