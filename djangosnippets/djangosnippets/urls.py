from django.contrib import admin
from django.urls import path
from snippets.views import top

urlpatterns = [
    path('', top, name='top'),
    path('admin/', admin.site.urls),
]
