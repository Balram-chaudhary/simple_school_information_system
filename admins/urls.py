from django.urls import path
from . import views
from admins.views import index, dashboard

app_name = 'admins'  # This registers the 'base' namespace

urlpatterns=[

   path('user/login/',views.index,name='user_login'),
   path('user/student/add', views.studentadd, name='studentadd'),
   path('user/student/edit/<int:id>/', views.studentedit, name='studentedit'),
   path('user/student/delete/<int:id>/', views.studentdelete, name='studentdelete'),

]

