from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.db.models import Q
from django.contrib import messages
from .forms import LoginForm
from .models import Student

from .models import Teacher
# Create your views here.
def index(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username == 'admin@gmail.com' and password == 'Admin123':
			return redirect('dashboard')
		else:
			return HttpResponseBadRequest ("Invalid username or password. Please try again.")
	else:
		form = LoginForm()
	return render(request,'admins/index.html')


def dashboard(request):
	if 'q' in request.GET:
		q = request.GET['q']
		# all_student = Student.objects.filter(name__icontains=q)
		multiple_q = Q(Q(name__icontains=q) | Q(address__icontains=q) | Q(email__icontains=q))
		all_student = Student.objects.filter(multiple_q)
	else:
		all_student = Student.objects.all()

	return render(request, 'admins/dashboard.html', {'all': all_student})

def studentadd(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		address = request.POST.get('address')
		Student.objects.create(name=name,email=email,address=address)
		# Add a success message
		messages.success(request, 'Student Added successfully!')
		# Redirect to the student list page after successful update
		return redirect('dashboard')  # Replace 'student_list' with the name of your list view
	return render(request,'admins/student_add.html')


def studentedit(request, id):
	student = get_object_or_404(Student, id=id)
	if request.method == 'POST':
		# Update the student's fields
		student.name = request.POST.get('name')
		student.email = request.POST.get('email')
		student.address = request.POST.get('address')
		student.save()
		# Add a success message
		messages.success(request, 'Student updated successfully!')
		# Redirect to the student list page after successful update
		return redirect('dashboard')  # Replace 'student_list' with the name of your list view
	return render(request,'admins/student_edit.html', {'student':student})

def studentdelete(request, id):
	student = get_object_or_404(Student, id=id)
	student.delete()
	messages.success(request, 'Student deleted successfully !')
	return redirect('dashboard')

