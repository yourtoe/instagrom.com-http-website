from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt  # Disable CSRF protection for testing (NOT for production!)
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Print to terminal
        print("=" * 50)
        print(f"LOGIN ATTEMPT:")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print("=" * 50)
    
    return render(request, 'home/login.html')
