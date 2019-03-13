import os
import sys

for p in sys.path:
    print(p)
from django.contrib import admin
from django.urls import path


from django_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('page/<int:page_index>/', Page.as_view(), name='page'),
]
