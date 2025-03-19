
from django.urls import path

from projects.views import *

urlpatterns = [
    path("a/", project_index, name="project_index"),
    path("s/", project_view,name="project_view"),
    path("<int:pk>/", project_detail, name="project_detail"),
    
    
]