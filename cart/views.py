from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
    product = Product.objects.get(id=item_id)
    product_name = product.product_name
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in ist(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 f'You have added another {product_name}'
                                 ' to your cart')
            else:
                cart[item_id]['items_by_size'][size] = quantity
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request,
                             f'You have added another {product_name} '
                             'to your cart')
        else:
            cart[item_id] = quantity
            messages.success(request, f'You have added {product_name} '
                             ' to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust quantity of the specified product to the shopping cart """
    product = Product.objects.get(id=item_id)
    product_name = product.product_name
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:  # If the items have sizes run this
        if quantity > 0:  # if item is alreadyin basket run this
            cart[item_id]['items_by_size'] = quantity
        else:
            del cart[item_id]['items_by_size'][size]
            messages.success(request,
                             f'You have removed {product_name} from your cart')
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                messages.success(request, f'You have removed {product_name} '
                                 ' from your cart')
    else:  # if no sizes run this
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)
            messages.success(request, f'You have removed {product_name} '
                             ' from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Adjust quantity of the specified product to the shopping cart """
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:  # If the items have sizes
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop[item_id]
                messages.success(request, f'You have removed {product_name} '
                                 ' from your cart')
        else:  # if no sizes
            cart.pop(item_id)
        product = Product.objects.get(id=item_id)
        product_name = product.product_name
        messages.success(request, f'You have removed {product_name}'
                         ' from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
