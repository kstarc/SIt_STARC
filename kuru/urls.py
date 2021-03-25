
from django.contrib import admin
from django.urls import path

from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flex/', views.flex, name='flex'),
    path('flex2/', views.flex2, name='flex2'),
]
