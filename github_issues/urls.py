from django.contrib import admin
from django.urls import path, include, re_path
from .views import All_Issues

urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path(r'^issues/(?P<username>\w+)/$', All_Issues.as_view())
    path('issues/<str:repo>/<str:repo_name>', All_Issues.as_view(), name='bio'),
]