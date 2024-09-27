from django.shortcuts import render


# Create your views here.

def index(request):
	# messages.success(request, 'Incorrect Username or Password')
	return render(request,'base/index.html')

