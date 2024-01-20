from django.shortcuts import render
from django.http import HttpResponse
from io import StringIO
import sys

def print_example(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        try:
            # Redirect stdout to capture print output
            original_stdout = sys.stdout
            sys.stdout = StringIO()

            # Try to execute the user input as Python code
            exec(user_input)

            # Get the printed output
            printed_output = sys.stdout.getvalue()

            # Reset stdout
            sys.stdout = original_stdout

            context = {'user_input': user_input, 'result': printed_output}

        except Exception as e:
            # Handle errors, if any
            context = {'user_input': user_input, 'error': str(e)}

        return render(request, 'pythonpractice/print_example.html', context)

    return render(request, 'pythonpractice/print_example.html')
