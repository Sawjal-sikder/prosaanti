from .models import Website

def global_context(request):
    context = {}
    
    # Add website info
    try:
        context['website'] = Website.objects.first()
    except Website.DoesNotExist:
        context['website'] = None

    # Add logged-in user info
    if request.user.is_authenticated:
        context['current_user'] = request.user

    return context
