from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'HomeTemp/home.html')

def login_view(request):
    return render(request, 'HomeTemp/loginP.html')
