from django.shortcuts import render
from .models import *

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

def Pdf(request):
    pdfs = Pdf.objects.all()
    return render(request, 'pdf.html', {'pdfs': pdfs})