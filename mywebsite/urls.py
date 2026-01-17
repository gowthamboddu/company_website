from django.contrib import admin
from django.urls import path, include
from contact.views import home, contact_view
urlpatterns = [
 path('admin/', admin.site.urls),
 path('', home, name='home'),
 path('contact/', include('contact.urls')),
]
