from django.urls import path, include


urlpatterns = [
    path('', include('users.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    
]