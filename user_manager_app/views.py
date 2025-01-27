from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .utils import role_required

@role_required(['instructor'])
def instructor_dashboard(request):
    return render(request, 'instructor_dashboard.html')

@role_required(['student'])
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@role_required(['admin'])
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
