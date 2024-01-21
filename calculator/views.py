# calculator_app/views.py
from django.shortcuts import render
from django.http import HttpResponse

from art import logo  # Assuming 'logo' is the ASCII art you want to display

def calculator(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        operation_symbol = request.POST['operation']
        num2 = float(request.POST['num2'])

        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y if y != 0 else "Error: Division by zero",
        }

        result = operations.get(operation_symbol, lambda x, y: "Error: Invalid operation")(num1, num2)

        return render(request, 'calculator_app/calculator.html', {'logo': logo, 'result': result})

    return render(request, 'calculator_app/calculator.html', {'logo': logo})
