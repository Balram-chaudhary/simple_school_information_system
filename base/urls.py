from django.urls import path
from . import views
app_name = 'base'  # This registers the 'base' namespace

urlpatterns=[
   path('',views.index),
]

