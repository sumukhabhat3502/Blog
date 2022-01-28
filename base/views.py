from django.http import HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Comment, Post
from .forms import CommentForm, PostForm, EditForm
from django.contrib.auth import get_user

# Create your views here.
# def home(reqeust):
#     return render(reqeust,'home.html',{})


def Like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))


class Home(ListView):
    model = Post  # which model to use
    template_name = 'home.html'
    ordering = ['-post_date']  # To sort the blogs by date

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class Detail(DetailView):
    model = Post
    template_name = 'detailed.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Detail, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()  # function from models.py
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class PostAdd(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_add.html'
    # fields= '__all__' # all the fileds in the data base
    # Can't have fields while using form_class


class CategoryAdd(CreateView):
    model = Category
    template_name = 'cat_add.html'
    fields = '__all__'


class Update_Post(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'


class Delete_Post(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')  # Used for deleteview


def CategoryView(request, cat):  # cat is variable in urls.py
    # category because the name is used in models.py
    category_post = Post.objects.filter(category=cat)
    return render(request, 'categories.html', {'cat': cat, 'category_post': category_post})


class CommentAdd(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('detail')

    # fields= '__all__' # all the fileds in the data base
    # Can't have fields while using form_class
