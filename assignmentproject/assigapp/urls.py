from django.urls import path

from assigapp import views

urlpatterns = [
    path('',views.register,name='reg'),
]