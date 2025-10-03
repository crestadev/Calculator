from django.contrib import admin
from django.urls import include, path
from calcul import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("calcul.urls")),
]
