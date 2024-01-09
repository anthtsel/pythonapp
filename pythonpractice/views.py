from django.shortcuts import render
from django.http import HttpResponse

def print_example(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        try:
            # Try to execute the user input as Python code
            result = eval(user_input)
            context = {'user_input': user_input, 'result': result}
        except Exception as e:
            # Handle errors, if any
            context = {'user_input': user_input, 'error': str(e)}
        return render(request, 'pythonpractice/print_example.html', context)

    return render(request, 'pythonpractice/print_example.html')
