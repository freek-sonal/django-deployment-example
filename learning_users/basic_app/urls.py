from django.contrib import admin
from django.urls import path,include
from basic_app import views

app_name = "basic_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",views.register,name='register'),

]
