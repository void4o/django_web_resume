from django.urls import path
from django_web_resume.resume_page.views import show_title, show_weapons


urlpatterns = [
    path('', show_title),
    path('weapons/', show_weapons)
]
