from django.urls import path
from . import views

urlpatterns = [
    path('', views.all),
    path('resume/', views.resume),
    path('social/', views.socials),
    path('education/', views.education),
]
