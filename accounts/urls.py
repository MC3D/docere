from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('authtools.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
