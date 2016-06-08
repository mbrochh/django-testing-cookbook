from django import forms

from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('body', )

    def clean_body(self):
        data = self.cleaned_data.get('body')
        if len(data) < 10:
            raise forms.ValidationError('Please enter at least 10 characters')
        return data
