from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from .models import Post
# Create your views here.

# function based view
'''
def indexView(request):
    """
    a function based view that renders the index.html template with a name context
    """
    name = "Motasem"
    context = {"name": name}
    return render(request, "index.html", context)
'''
class IndexView(TemplateView):
    """
    a class based view that renders the index.html template with a name context
    """
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        condext = super().get_context_data(**kwargs)
        condext["name"] = "Motasem"
        condext["posts"] = Post.objects.all()
        return condext
    
''' FBV for redirect view

from django.shortcuts import redirect
def redirectToMakatab(request):
    """
    a function based view that redirects to maktabkhooneh.org
    """
    return redirect("https://www.maktabkhoneh.org/")
    
'''

class RedirectToMaktab(RedirectView):
    url = "https://maktabkhooneh.org/"
    
class Postlist(ListView):
    '''
    We use it to get post.
    '''
    # model = Post
    # queryset = Post.objects.all()
    context_object_name = 'posts'
    
    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return super().get_queryset()
    
