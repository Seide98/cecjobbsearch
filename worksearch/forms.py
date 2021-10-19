from django import forms
from .models import Post, PostPlan, PostUserSett, PostUserUpload

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'company', 'link', 'free_text_field', 'choises_activity', 'city')
        exclude = ('user',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'choises_activity': forms.Select(attrs={'class': 'form-control'}),
            'free_text_field': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PlannedForm(forms.ModelForm):
    class Meta:
        model = PostPlan
        fields = ('title', 'company', 'link', 'last_app_date', 'free_text_field', 'choises_activity', 'city')
        exclude = ('user',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'choises_activity': forms.Select(attrs={'class': 'form-control'}),
            'last_app_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'type':'date'}),
            'free_text_field': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UserSettForm(forms.ModelForm):
    class Meta:
        model = PostUserSett
        fields = ('title', 'link')
        exclude = ('user',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PostUserForm(forms.ModelForm):
    class Meta:
        model = PostUserUpload
        fields = ('document',)
        exclude = ('user',)

        widgets = {
            'document': forms.FileInput(attrs={'class': 'form-control'}),
        }