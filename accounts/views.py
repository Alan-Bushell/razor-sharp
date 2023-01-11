from django.shortcuts import (redirect,
                              get_object_or_404,
                              render)
from checkout.models import Order
from .models import UserProfile, Account
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .forms import AccountForm, ImageForm
from django.contrib import messages


# Create your views here.


def accounts(request):
    """ A view to return profile page """
    template = 'accounts/account.html'
    return render(request, template)


def shipping_details(request):
    """ A view to return profile page """
    return render(request, 'accounts/shipping_details.html')


def order_history(request):
    """ A view to return profile page """
    orders = Order.objects.all()
    template = 'accounts/order_history.html'
    context = {
        'orders': orders
    }
    return render(request, template, context)


def edit_profile(request, user_id):
    """View to allow updating user account info"""
    account = get_object_or_404(Account, id=user_id)
    form = AccountForm(instance=account)
    if request.POST:
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your profile has been updated')
        return redirect('accounts')
    account = AccountForm(instance=account)
    context = {
        'form': form
    }
    template = 'accounts/edit_profile.html'
    return render(request, template, context)


def edit_image(request, user_id):
    user = get_object_or_404(Account, id=user_id)
    userprofile = get_object_or_404(UserProfile, user=user)
    if request.POST:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            userprofile.profile_picture = request.FILES['profile_picture']
            userprofile.save()
            form.save()
            messages.success(request,
                             'Your image has been updated')
        return redirect('accounts')

    user = get_object_or_404(Account, id=user_id)
    form = ImageForm(instance=userprofile)
    context = {
        'form': form
    }
    template = 'accounts/edit_image.html'
    return render(request, template, context)


def edit_shipping(request, user_id):
    """View to allow updating user shipping info"""
    profile = get_object_or_404(UserProfile, id=user_id)
    form = UserProfileForm(instance=profile)
    if request.POST:
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your profile has been updated')
        return redirect('accounts')
    profile = UserProfileForm(instance=profile)
    context = {
        'form': form
    }
    template = 'accounts/edit_profile.html'
    return render(request, template, context)


# Signal used to create user profile once user created
@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Signal used to save the profile if user is saved
@receiver(post_save, sender=Account)
def save_user_profile(sender, instance, created, **kwargs):
    instance.userprofile.save()
