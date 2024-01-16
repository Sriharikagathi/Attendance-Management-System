
from django.contrib import admin
from django.urls import path,include
from mylogin import views
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("mansys.urls"),name="mansys"),
    path("log/",include("mylogin.urls"),name="mylogin"),
    path("<str:semester>/<str:branch>/<str:section>/<str:subject>/",index,name="index"),
    # path('save_to_session/', save_to_session, name='save_to_session'),
]
