# 장고 폼을 담을 수 있는 파이썬 파일 만들기.

from django import forms
from .models import Blog

class BlogForm(forms.Form):
    #입력 받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['title', 'body']