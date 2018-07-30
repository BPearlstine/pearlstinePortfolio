from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Comic


class AddComicForm(forms.Form):
    title = forms.CharField(required=True)
    issue = forms.CharField(required=True)
    graded = forms.CharField(required=True)
    key = forms.CharField(required=True)
    publisher = forms.CharField(required=True)

    def cleanNewComic(self):
        title = self.cleaned_data['title']
        issue = self.cleaned_data['issue']
        graded = self.cleaned_data['graded']
        key = self.cleaned_data['key']
        publisher = self.cleaned_data['publisher']
        
        for comic in Comic.objects.all():
            if comic.title == title and comic.issue == issue:
                raise ValidationError(
                    _('This book is already logged'))

        return title,issue,graded,key,publisher
