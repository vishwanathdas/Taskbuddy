
from django.contrib import admin
from django.urls import path, include
from account.views import LoginView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls"), name="account"),
    path("task/", include("task.urls"), name="task"),
    path("",LoginView.as_view(),name="home")  
]
