from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.TodoList.as_view(), name='tasks'),
    path('form-create', views.CreateTask.as_view(), name='form-create'),
    path('form-update/<int:pk>/', views.UpdateTask.as_view(), name='form-update'),
    path('form-delete/<int:pk>/', views.DeleteTask.as_view(), name='form-delete'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register')
]
