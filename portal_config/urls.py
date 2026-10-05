from django.contrib import admin
from django.urls import path
from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.entry_form_view, name='registration_entry'),
    path('summary/', views.summary_view, name='registration_summary'),
]