from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'HomeTemp/home.html')

def login_view(request):
    return render(request, 'HomeTemp/loginP.html')

def features(request):
    return render(request, 'HomeTemp/features.html')

def testmonials(request):
    return render(request, 'HomeTemp/testmonials.html')
