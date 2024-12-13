from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'quotes'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='quotes_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='quotes_app:login'), name='logout'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('authors/', views.author_list, name='authors'),
    path('', views.quote_list, name='quotes'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
]


