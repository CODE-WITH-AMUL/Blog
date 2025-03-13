from django.shortcuts import render
from .models import Blog, Pdf

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

def pdf_list(request):  # Fixed function name (use lowercase)
    pdfs = Pdf.objects.all()
    return render(request, 'pdf.html', {'pdfs': pdfs})
