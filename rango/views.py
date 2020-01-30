from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category, Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    
    # Construct a dictionary to pass variables to the template engine.
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    # Return a rendered response with the template we wish to use to send to the client.
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'myname': 'yuuto'}
    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        # Try to find a category with given category_name_slug.
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        pages = Page.objects.filter(category=category)
        # Add them in the dictionary.
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        # Set the values to None when we can't find the category.
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context=context_dict)