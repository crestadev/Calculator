from django.contrib import admin
from django.urls import path
from calcul import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calculator, name='calculator'),
]
