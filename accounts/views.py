from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user-role')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            
            # Redirect based on user type
            if user.user_type == 'student_working':
                return redirect('student_dashboard')
            elif user.user_type == 'supervisor':
                return redirect('supervisor_dashboard')
            elif user.user_type == 'director':
                return redirect('director_dashboard')
            elif user.user_type == 'admin' or user.is_superuser:  # Added is_superuser check
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'Invalid user type')
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')

@login_required
def student_dashboard(request):
    return render(request, 'dashboard.html', {'user_type': 'student'})

@login_required
def supervisor_dashboard(request):
    return render(request, 'wsdirector/drt.html', {'user_type': 'supervisor'})

@login_required
def director_dashboard(request):
    return render(request, 'wsdirector/drt.html', {'user_type': 'director'})

@login_required
def admin_dashboard(request):
    # Get statistics for the dashboard
    total_students = User.objects.filter(user_type='student_working').count()
    active_assignments = 0  # You'll need to implement this based on your work assignment model
    total_departments = 5  # Replace with actual department count when you implement departments
    total_hours = 0  # Replace with actual hours calculation

    # Mock recent activities - replace with actual activity tracking
    recent_activities = [
        {
            'description': 'New student registration: John Smith',
            'timestamp': timezone.now() - timedelta(hours=2)
        },
        {
            'description': 'Work assignment updated: Library Services',
            'timestamp': timezone.now() - timedelta(hours=5)
        },
        {
            'description': 'Monthly report generated',
            'timestamp': timezone.now() - timedelta(days=1)
        }
    ]

    context = {
        'user_type': 'admin',
        'total_students': total_students,
        'active_assignments': active_assignments,
        'total_departments': total_departments,
        'total_hours': total_hours,
        'recent_activities': recent_activities,
    }
    
    return render(request, 'admin_dashboard.html', context)
