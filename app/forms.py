from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Booking, Profile,RATE_RIDE,Review
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

class CreateProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['profile_photo','bio','phone_number','Id_number']
        widgets = {
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            # 'profile_photo':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'Id_number':forms.TextInput(attrs={'class':'form-control'}),
        
            
        }
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields=['duration']
class RatingsForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}),required=False)
    rate_ride= forms.ChoiceField(choices=RATE_RIDE,required=True,widget=forms.Select())
    
    class Meta:
        model = Review
        fields = ['body','rate_ride']