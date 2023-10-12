from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label="username",max_length=10)
    message_input = forms.CharField(label="Message",max_length=100,
                                    widget=forms.Textarea(attrs={"class":"twtmessage"}))
    
class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["username", "message"]   



