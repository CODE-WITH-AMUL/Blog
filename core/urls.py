from django.urls import path
from .views import blog, pdf_list

urlpatterns = [
    path('', blog, name='blog'),
    path('pdf/', pdf_list, name='pdf_list')  # Fixed name (removed extra space)
]
