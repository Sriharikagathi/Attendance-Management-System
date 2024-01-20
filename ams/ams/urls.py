
from django.contrib import admin
from django.urls import path,include
from mylogin import views
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("mylogin.urls"),name="mylogin"),
    # path("log/",include("mylogin.urls"),name="mylogin"),
    path("<str:semester>/<str:branch>/<str:section>/<str:subject>/",index,name="index"),
    # path('save_to_session/', save_to_session, name='save_to_session'),
    path('attendance/',attendance,name="attendance")
]
