from django.contrib import admin
from django.urls import path, include  # Include 'include'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PersonalPortfolioApp.urls')),  # Add this line
]
