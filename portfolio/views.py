from django.shortcuts import render
from django.core.mail import send_mail
from Port.forms import PortfolioContactForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def home(request):
    form = PortfolioContactForm()
    if request.method == "POST":
        form = PortfolioContactForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            #return HttpResponse('Message succesful')
            return HttpResponseRedirect('/')
            form.save()
        else:
            form()
    context = {
        'form': form
    }
    template_name = 'index.html'
    return render(request, template_name, context)