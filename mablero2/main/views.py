from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'contacts': 'contacts/'
    }
    return render(request, 'main/index.html', context)

def contacts(request):
    return render(request, 'main/contacts.html')
