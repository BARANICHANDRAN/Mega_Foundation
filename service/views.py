from django.shortcuts import render,redirect
from .models import Issue,Volunteer
from .forms import issueform, volunteerform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout 

def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_page')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def admin_page(request):
    total_issues = Issue.objects.count()
    total_volunteers = Volunteer.objects.count()
    return render(request, 'admin.html', {
        'total_issues': total_issues,
        'total_volunteers': total_volunteers
    })

@login_required(login_url='login')
def issue_list(request):
    issues = Issue.objects.all()
    locations = Issue.objects.values_list('location', flat=True).distinct()
    issue_types = Issue.objects.values_list('issue_type', flat=True).distinct()
    
    # Get filter parameters
    location = request.GET.get('location')
    issue_type = request.GET.get('issue_type')
    
    # Apply filters
    if location:
        issues = issues.filter(location=location)
    if issue_type:
        issues = issues.filter(issue_type=issue_type)
    
    return render(request, 'issue_list.html', {
        'issues': issues,
        'locations': locations,
        'issue_types': issue_types,
        'selected_location': location,
        'selected_type': issue_type
    })

@login_required(login_url='login')
def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    locations = Volunteer.objects.values_list('location', flat=True).distinct()
    work_areas = Volunteer.objects.values_list('work_area', flat=True).distinct()
    
    # Get filter parameters
    location = request.GET.get('location')
    work_area = request.GET.get('work_area')
    
    # Apply filters
    if location:
        volunteers = volunteers.filter(location=location)
    if work_area:
        volunteers = volunteers.filter(work_area=work_area)
    
    return render(request, 'volunteer_list.html', {
        'volunteers': volunteers,
        'locations': locations,
        'work_areas': work_areas,
        'selected_location': location,
        'selected_work_area': work_area
    })

def add_issue(request):
    if request.method == 'POST':
        form = issueform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = issueform()
    return render(request, 'add_issue.html', {'form': form})


def add_volunteer(request):
    if request.method == 'POST':
        form = volunteerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = volunteerform()
    return render(request, 'add_volunteer.html', {'form': form})

