from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def students(request):
  sdt = StudentDetails.objects.all().order_by('id')
  pagination = Paginator(sdt,2) 
  page_no = request.GET.get('page')
  studentdetails = pagination.get_page(page_no)
  pagelist = pagination.page(page_no)

  content = {
    'StudentDetails':studentdetails,
    'PageList':pagelist
  }
  return render(request,"index.html",content)