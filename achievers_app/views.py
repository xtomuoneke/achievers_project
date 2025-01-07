from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def our_values(request):
    return render(request, 'our_values.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def course_secondary(request):
    return render(request, 'course_secondary.html')

def gallery(request):
    return render(request, 'gallery.html')

def FAQ(request):
    return render(request, 'FAQ.html')

def higher_secondary(request):
    return render(request, 'higher_secondary.html')

def other_course(request):
    return render(request, 'other_course.html')

def our_team(request):
    return render(request, 'our_team.html')