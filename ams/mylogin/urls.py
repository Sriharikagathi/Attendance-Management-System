
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("facultyInfo/",views.facultyInfo,name="facultyInfo"),
    path("logout/",views.logout,name="logout"),
    path("studentlist/",views.studentlist,name="studentlist"),
]
