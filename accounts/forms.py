from django import forms
from django.contrib.auth.forms import UserCreationForm
from doctor.models import TimeSchedule
from administrator.models import *
from . models import CustomUser

class CreatePatientForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'is_patient']

class AdminCreatePatientForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'is_patient']

class AdminCreateDoctorForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'is_doctor']

class TimeScheduleForm(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    
    class Meta:
        model = TimeSchedule
        fields = ['weekday', 'start_time', 'end_time', 'duration']
        exclude = ['doctor']


class AddSliderBannerForm(forms.ModelForm):
    
    class Meta:
        model = SliderBanner
        fields = ['banner_title', 'banner_description', 'banner_image']



class AddServicesForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ['service_title', 'service_description', 'service_image']

class AddAboutForm(forms.ModelForm):
    
    class Meta:
        model = About
        fields = ['about_title', 'about_description', 'about_image']


class AddBlogPostForm(forms.ModelForm):
    
    class Meta:
        model = BlogPost
        fields = ['blog_title', 'blog_description','blog_body', 'blog_image']

class AddPageSettingForm(forms.ModelForm):
    opening_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    closing_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    
    class Meta:
        model = PageSetting
        fields = ['company_name', 'company_address','company_phone', 'company_email', 'company_facebook_id', 'company_twitter_id', 'company_linkedin_id','company_skype_id','opening_time', 'closing_time','company_currency', 'company_logo']

