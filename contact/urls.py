from django.contrib import admin
from django.urls import path
from contact.views import home, contact_view
app_name = 'contact'   # ✅ THIS IS REQUIRED
urlpatterns = [
 path('add/', contact_view, name='add_contact'),
]
