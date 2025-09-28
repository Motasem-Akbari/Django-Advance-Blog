from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView,DeleteView
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Post
from .forms import PostForm


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


class PostlistView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    '''
    We use it to get post.
    '''
    permission_required = 'blog.view_post'
    # model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    # paginate_by = 2
    ordering = 'id'

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(DetailView):
    model = Post

'''
class PostCreateView(FormView):
    template_name = "blog/contact.html"
    form_class = PostForm
    success_url = "/blog/post/"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''


class PostCreateView(CreateView):
    model = Post
    # fields = ['author','title','content','status','category','published_date']
    form_class = PostForm   # ****
    success_url = '/blog/post'
        
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'



class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/post'