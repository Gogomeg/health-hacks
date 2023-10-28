from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)
from .forms import RecipeForm
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm
from .forms import ImageForm



# Render a list with the objects of the specified model


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

# How the posts are shown


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'post_deteail.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
        return render(request, 'post_detail.html', {'form': form})


class Health_hacks(ListView):
    """View all health hacks"""

    template_name = "health_hacks/health_hacks.html"
    model = Recipe
    context_object_name = "health_hacks"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            health_hacks = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query) |
                Q(cuisine_types__icontains=query)
            )
        else:
            health_hacks = self.model.objects.all()
        return health_hacks


class HackDetail(DetailView):
    """View a single health hack"""

    template_name = "health_hacks/post_detail.html"
    model = Recipe
    context_object_name = "healt_hack"


class AddHack(LoginRequiredMixin, CreateView):
    """Add health hacks view"""

    template_name = "health_hacks/add_health_hack.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/health_hacks/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddHack, self).form_valid(form)


class EditHack(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a health hack"""
    template_name = 'health_hacks/edit_health_hack.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/healt_hacks/'

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteHack(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a health hack"""
    model = Recipe
    success_url = '/health_hacks/'

    def test_func(self):
        return self.request.user == self.get_object().user
