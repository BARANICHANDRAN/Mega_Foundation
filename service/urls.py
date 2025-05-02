from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_issue, name='add_issue'),
    path('volunteer/', views.add_volunteer, name='add_volunteer'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('success/', views.success, name='success'),
    path('issues/', views.issue_list, name='issue_list'),
    path('volunteers/', views.volunteer_list, name='volunteer_list'),
    path('', views.home, name='home'),
]