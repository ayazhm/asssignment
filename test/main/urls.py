from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('diseasetype/', views.type, name='type'),
    path('disease/', views.disease, name='disease'),
    path('country/', views.country, name='country'),
    path('users/', views.users, name='users'),
    path('doctors/', views.doctors, name='doctors'),
    path('specialize/', views.specialize, name='specialize'),
    path('publicservant/', views.publicservant, name='publicservant'),
    path('discover/', views.discover, name='discover'),
    path('record/', views.record, name='record'),
    path('add_type/', views.add_type, name='add_type'),
    path('delete_type/<int:pk>', views.delete_type, name='delete_type'),
    path('update_type/<int:pk>', views.update_type, name='update_type'),
    path('add_disease/', views.add_disease, name='add_disease'),
    path('update_disease/<slug:pk>', views.update_disease, name='update_disease'),
    path('delete_disease/<slug:pk>', views.delete_disease, name='delete_disease'),
    path('add_country/', views.add_country, name='add_country'),
    path('delete_country/<slug:pk>', views.delete_country, name='delete_country'),
    path('update_country/<slug:pk>', views.update_country, name='update_country'),
    path('add_user/', views.add_user, name='add_user'),
    path('update_user/<pk>', views.update_user, name='update_user'),
    path('delete_user/<pk>', views.delete_user, name='delete_user'),
]