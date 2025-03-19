
from django.shortcuts import render
from .forms import ContactForm

  
# Create your views here.
def contact_view(request):
    form = ContactForm()
    context = {'form': form}
    template_name = 'contact.html'
    if form.is_valid():
        form.save()
    return render(request, template_name, context)