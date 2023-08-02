
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal/', include('personal.urls')),
    path('polls/', include('polls.urls')),
    path('user_auth/', include('user_auth.urls', namespace='user_auth')),
]
