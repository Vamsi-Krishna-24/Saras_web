from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'Home/home.html')

def login_view(request):
    return render(request, 'Home/loginP.html')

def features(request):
    return render(request, 'Home/features.html')

def testmonials(request):
    return render(request, 'Home/testmonials.html')
