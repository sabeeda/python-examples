
from django.shortcuts import render
from projects.models import Project
from .forms import ProjectForm
from django.core.paginator import Paginator
from .models import Project
# import viewsets
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
# import local data
from .serializers import ProjectSerializer



def project_index(request):
    projects = Project.objects.all()
    paginated = Paginator(projects, 2)
    page_number = request.GET.get('page') #Get the requested page number from the URL
    
    page = paginated.get_page(page_number)
    context = {
        "page": page
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)

def project_view(request):
    form = ProjectForm(request.POST or None)
    context = {'form': form}
    template_name = 'project_entry.html'
    if form.is_valid():
        form.save()
    return render(request, template_name, context)

class projectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

      
    