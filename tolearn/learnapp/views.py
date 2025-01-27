
from django.shortcuts import render,redirect
from . import views
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.


def home(request):   
    return render(request,'index.html' )

# let me use logout building functinality that dose the view work underground
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfuly.')
        return redirect('home')
    else:
        return render(request, 'logout.html')
    
def AboutCoachingC(request):
    return render(request,'AboutCoachingC.html')

def our_values(request):
    return render(request,'our_values.html')

def our_team(request):
    return render(request,'our_team.html')

def course_secoundary(request):
    return render(request,'course_secoundary.html')

def higher_secoundary(request):
    return render(request,'higher_secoundary.html')

def othercourse(request):
    return render(request,'othercourse.html')

def gallery(request):
    return render(request,'gallery.html')

def FAQ(request):
    return render(request,'FAQ.html')

def contact_us(request):
    return render(request,'contact_us.html')


