from django.shortcuts import render


# Create your views here.
def home(request):
    title = 'Home Page'
    context = {'title': title}
    template = 'home.html'
    return render(request, template, context)


def about(request):
    title = 'Home Page'
    context = {'title': title}
    template = 'about.html'
    return render(request, template, context)
