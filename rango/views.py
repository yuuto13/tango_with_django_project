from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # Construct a dictionary to pass variable {{boldmessage}} to the template engine.
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response with the template we wish to use to send to the client.
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'myname': 'yuuto'}
    return render(request, 'rango/about.html', context=context_dict)