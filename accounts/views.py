from django.shortcuts import (redirect,
                              get_object_or_404,
                              render)
from checkout.models import Order
from .models import UserProfile, Account
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
from .forms import AccountForm, ImageForm, AddressForm
from django.contrib import messages


# Create your views here.


@login_required
def accounts(request):
    """ A view to return profile page """
    template = 'accounts/account.html'
    return render(request, template)


@login_required
def shipping_details(request):
    """ A view to return profile page """
    return render(request, 'accounts/shipping_details.html')


@login_required
def order_history(request):
    """ A view to return profile page """
    orders = Order.objects.all()
    template = 'accounts/order_history.html'
    context = {
        'orders': orders
    }
    return render(request, template, context)


@login_required
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


@login_required
def edit_image(request, user_id):
    user = get_object_or_404(Account, id=user_id)
    userprofile = get_object_or_404(UserProfile, user=user)
    if request.POST:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            userprofile.profile_picture = request.FILES['profile_picture']
            userprofile.save()

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


@login_required
def edit_shipping(request, user_id):
    """View to allow updating user shipping info"""
    profile = get_object_or_404(UserProfile, user=user_id)
    form = AddressForm(instance=profile)
    if request.POST:
        form = AddressForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your profile has been updated')
        return redirect('accounts')
    profile = AddressForm(instance=profile)
    context = {
        'form': form
    }
    template = 'accounts/edit_shipping.html'
    return render(request, template, context)


@login_required
def delete_account(request, user_id):
    """Delete users account"""
    user = get_object_or_404(Account, id=user_id)
    user.delete()
    messages.warning(request,
                     "Your account has been closed.")
    return redirect('home')


def order_history_details(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

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
