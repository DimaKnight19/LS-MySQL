from django.contrib import admin
from django.urls import path, include
from ls.views import login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ls/', include('ls.urls', namespace="ls")),
    path('', login_view, name="login_view")
    
]