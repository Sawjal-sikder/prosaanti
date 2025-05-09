from django import forms
from home.models import Website

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = '__all__' 
        widgets = {
            # 'address': forms.Textarea(attrs={
            #     'rows': 2,
            #     'class': 'w-full text-sm  border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:outline-none',
            # }),
            # 'name': forms.TextInput(attrs={
            #     'class': 'w-full text-sm  border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:outline-none',
            #     'placeholder': 'Enter website name',
            # }),
            # 'phone': forms.TextInput(attrs={
            #     'class': 'w-full text-sm  border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:outline-none',
            #     'placeholder': 'Enter phone number',
            # }),
            # 'website': forms.URLInput(attrs={
            #     'class': 'w-full text-sm  border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:outline-none',
            #     'placeholder': 'Enter website URL',
            # }),
            # 'email': forms.EmailInput(attrs={
            #     'class': 'w-full text-sm  border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:outline-none',
            #     'placeholder': 'Enter email address',
            # }),
            # 'facebook': forms.URLInput(attrs={
            #     'class': 'w-full text-sm  border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:outline-none',
            #     'placeholder': 'Enter Facebook URL',
            # }),
            # 'youtube': forms.URLInput(attrs={
            #     'class': 'w-full text-sm  border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:outline-none',
            #     'placeholder': 'Enter YouTube URL',
            # }),
            'logo': forms.ClearableFileInput(attrs={
                'class': 'block w-full  text-gray-900 border border-gray-300 rounded-full cursor-pointer bg-gray-50 focus:outline-none',
                'aria-describedby': 'logo_help',
                'id': 'logo_input',
            }),
            'fabicon': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-full cursor-pointer bg-gray-50 focus:outline-none',
                'aria-describedby': 'fabicon_help',
                'id': 'fabicon_input',
            }),
        }
