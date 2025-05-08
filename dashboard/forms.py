from django import forms
from home.models import Website

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = '__all__' 
        widgets = {
            'address': forms.Textarea(attrs={
                'rows': 2,
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                'placeholder': 'Enter website name',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                'placeholder': 'Enter phone number',
            }),
            'website': forms.URLInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                'placeholder': 'Enter website URL',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                'placeholder': 'Enter email address',
            }),
            'facebook': forms.URLInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                'placeholder': 'Enter Facebook URL',
            }),
            'youtube': forms.URLInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                'placeholder': 'Enter YouTube URL',
            }),
            'logo': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                'aria-describedby': 'user_avatar_help',
                'id': 'user_avatar',
            }),
            'fabicon': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                'aria-describedby': 'user_avatar_help',
                'id': 'user_avatar',
            }),
        }
