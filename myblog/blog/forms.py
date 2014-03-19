#-*- coding:utf-8 -*-
from django import forms
from blog.models import Category
from blog.models import AuthorInfo


class ContactForm(forms.Form):
    cateList = []
    cate = Category.objects.all()
    for item in cate:
        cateList.append((item.id, item.name), )

    cateTuple = tuple(cateList)

    authorList = []
    authorInfo = AuthorInfo.objects.all()
    for item in authorInfo:
        authorList.append((item.id, item.name))

    authorTuple = tuple(authorList)

    h1 = forms.CharField(widget=forms.TextInput(attrs={"class": "fn-form-input"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "fn-form-area"}))
    music_url = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={"class": "fn-form-input", "placeholder": " 可以为空"}))
    author = forms.CharField(widget=forms.TextInput(attrs={"class": "fn-form-input"}))
    author = forms.ChoiceField(choices=authorTuple, widget=forms.Select(attrs={"class": "fn-form-select"}))
    category = forms.ChoiceField(choices=cateTuple, widget=forms.Select(attrs={"class": "fn-form-select"}))