from django.shortcuts import render
from blog.models import Category

# Create your views here.
def home(request):
    categories= Category.objects.all()  # retrieves all the records from the Category table and stores them in the categories.
    context = {'cate':categories} # Creates a dictionary to pass the QuerySet to the template.
    # here 'cate' is a string key which will be used in templates to access the associate data.
    return render(request,'base.html')