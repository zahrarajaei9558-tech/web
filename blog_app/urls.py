from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome_view, name='welcome'),
    path('sum/', views.sum_view, name='sum'),
    path('<int:a>/<int:b>/', views.multiply_view, name='multiply'),
    path('rand/<int:user_number>/', views.random_game_view, name='random_game'),
    path('bmi/<int:height>/<int:weight>/', views.bmi_view, name='bmi'),
]
