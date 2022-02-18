from django.urls import path, include
from .router import router
from app import views

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name="home"),
]