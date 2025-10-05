from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome_view, name='welcome'),
    path('sum/', views.sum_view, name='sum'),
    path('<int:a>/<int:b>/', views.multiply_view, name='multiply'),
]
