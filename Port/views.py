from django.shortcuts import render

from .forms import PortfolioContactForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def home(request):
    form = PortfolioContactForm()
    if request.method == "POST":
        form = PortfolioContactForm(request.POST or None)
        if form.is_valid():
            return HttpResponseRedirect('/Port')
            form.save()
    context = {
        'form': form
    }
    template_name = 'index.html'
    return render(request, template_name, context)