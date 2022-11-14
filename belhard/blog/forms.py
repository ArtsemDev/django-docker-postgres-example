from django.forms import ModelForm

from .models import Comment, Newsletter


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'text', 'recomment', 'author')


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email', )
