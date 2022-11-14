from django.views.generic import ListView, DetailView

from .forms import CommentForm, NewsletterForm
from .models import Post, Comment


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    object = None

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        context['comments'] = Comment.objects.filter(post__id=context[self.context_object_name].id)
        context['comment_form'] = CommentForm()
        context['newsletter_form'] = NewsletterForm()
        return context

    def post(self, request, post_slug):
        if request.POST.get('form') == 'comment':
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
        elif request.POST.get('form') == 'newsletter':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
        return self.get(request=request, post_slug=post_slug)
