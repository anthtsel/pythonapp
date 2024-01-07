from django.shortcuts import render

def index(request):
    # Define context data to pass to the template
    context = {
        'welcome_message': 'Welcome to My Python Website!',
    }

    # Render the template with the provided context
    return render(request, 'website/index.html', context)