from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body','name', 'email')
    
    # overriding default form setting and adding bootstrap class
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        
        self.fields['body'].widget.attrs = {'placeholder': 'Your comment', 'class':'form-control','' 'rows':'5'}
        self.fields['name'].widget.attrs = {'placeholder': 'Nickname','class':'form-control','input type':'text','aria-label':'Nickname'}
        self.fields['email'].widget.attrs = {'placeholder': 'Email', 'class':'form-control','type':'email'}
        
   