from django.shortcuts import render

def post_list(request):
    return render(request, 'webpage1/post_list.html', {})


#from django.http import HttpResponse

#def index(request):
 #  return HttpResponse("<h1>This is the webpage</h1>")