from django.urls import path
from . import views

urlpatterns = [
    path('', views.dishs_home, name='dishs'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('<int:pk>/update', views.DishUpdateView.as_view(), name='dish-update')
]