from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.models import *
from .forms import *

# Dashboard (Admin only)
@login_required
def dashboard(request):
    if not request.user.is_superuser:
        messages.warning(request, "Access denied!")
        return redirect('home')
    return render(request, 'admin.html')

# Website Info (Admin only)
@login_required
def website_info(request):
    if not request.user.is_superuser:
        messages.warning(request, "Access denied!")
        return redirect('home')
    return render(request, 'settings/website_info.html')

# Website Info Update (Admin only)
@login_required
def website_info_update(request, pk):
    if not request.user.is_superuser:
        messages.warning(request, "Access denied!")
        return redirect('home')

    website = get_object_or_404(Website, pk=pk)
    form = WebsiteForm(request.POST or None, request.FILES or None, instance=website)

    if form.is_valid():
        form.save()
        messages.success(request, "Website information updated successfully")
        return redirect('website_info')

    return render(request, 'settings/form.html', {'form': form})
