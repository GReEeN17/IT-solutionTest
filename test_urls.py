from django.urls import path
from views import views

urlpatterns = [
    path('test/', views.parser),
    path('show/', views.show_db)
]