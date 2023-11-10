from django import forms
from .models import Post

class PostBasedForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    

class PostCreateForm(PostBasedForm):
    class Meta(PostBasedForm.Meta):
        fields = ['image', 'content']

class PostUpdateForm(PostBasedForm):
    class Meta(PostBasedForm.Meta):
        fields = ['image', 'content']

class PostdDetailForm(PostBasedForm):
    def __init__(self, *args, **kwargs):
        super(PostdDetailForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs['disabled'] = True