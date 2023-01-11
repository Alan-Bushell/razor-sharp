from django.shortcuts import (redirect,
                              get_object_or_404,
                              render)
from checkout.models import Order
from .models import UserProfile, Account
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .forms import AccountForm
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


# Signal used to create user profile once user created
@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Signal used to save the profile if user is saved
@receiver(post_save, sender=Account)
def save_user_profile(sender, instance, created, **kwargs):
    instance.userprofile.save()
