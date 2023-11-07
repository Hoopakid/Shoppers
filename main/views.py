import json
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .models import *
from django.http.response import JsonResponse

User = get_user_model()


class HomeTemplateView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        products = Product.objects.all()  # select * from main_product
        product_data = []
        comments = Comment.objects.all().order_by('-created_at')[:4]
        for product in products:
            image = Image.objects.filter(product=product).first()  #  select * from image where product_id=product_id
            product.image = image
            product_data.append(product)
        self.context.update({'product_data': product_data})
        self.context.update({'comments': comments})
        return render(request, self.template_name, self.context)

    def post(self, request):
        product_id = request.POST.get('product_id')
        if request.user is None:
            return redirect('accounts/login')
        user = request.user.id
        if not ShoppingCart.objects.filter(Q(user_id=user) & Q(product_id=product_id)).exists():
            shopping_cart = ShoppingCart.objects.create(
                user_id=user,
                product_id=product_id
            )
            shopping_cart.save()
            print('Product added to cart')
            return redirect(f'/#product_{product_id}')

        print('This product already exists in cart!')
        return redirect(f'/#product_{product_id}')


class ShoppingCartTemplateView(View):
    template_name = 'cart.html'
    context = {}

    def get(self, request):
        if request.user.id is None:
            return redirect('/accounts/login')
        shopping_cart = ShoppingCart.objects.filter(user=request.user)
        data = []
        for index, value in enumerate(shopping_cart):
            image = Image.objects.filter(product=value.product).first()
            value.image = image
            value.index = index+1
            data.append(value)
        self.context.update({'shopping_cart_products': data})
        return render(request, self.template_name, self.context)

    def post(self, request):
        shopping_cart_id = request.POST.get('shopping_cart_id')
        ShoppingCart.objects.get(pk=shopping_cart_id).delete()
        return redirect('/cart')


class IncrementCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            shopping_cart.count +=1
            shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class DecrementCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            if shopping_cart.count > 0:
                shopping_cart.count -= 1
                shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class ChangeCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            product_count = json_data.get('product_count')

            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            if product_count is not None:
                shopping_cart.count = product_count
                shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class AddProductView(View):
    template_name = 'add-product.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        name = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        images = request.FILES.getlist('images')

        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            author=request.user.id
        )
        product.save()
        for image in images:
            image = Image.objects.create(
                image=image,
                product_id=product
            )
            image.save()
        return redirect('/add-product')


class CommentView(View):
    template_name = 'comment.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        message = request.POST.get('message')
        is_anonymous = request.POST.get('is_anonymous')
        user = None if is_anonymous == 'on' else request.user.id

        comment = Comment.objects.create(
            message=message,
            user_id=user
        )
        comment.save()
        return redirect('/')


class CheckoutView(View):
    def post(self, request):
        user_id = request.POST.get('user_id')
        shopping_cart = ShoppingCart.objects.filter(user_id=user_id)


class OrderView(View):
    template_name = 'checkout.html'
    context = {}

    def get(self, request):
        product_data = Order.objects.select_related('product').filter(user_id=request.user.id)
        productss = []
        for product in product_data:
            image = Image.objects.filter(product_id=product.product.id).first()
            product.image = image
            productss.append(product)
        self.context.update({'product_data': productss})
        return render(request, self.template_name, self.context)

    def post(self, request):
        products = ShoppingCart.objects.select_related('product').filter(user_id=request.user.id)
        for product in products:
            order = Order.objects.create(
                user_id=request.user.id,
                product=product.product,
                count=product.count,
                status=1
            )
            order.save()
            ShoppingCart.objects.get(pk=product.id).delete()
        return redirect('/checkout')


def about(request):
    return render(request, 'about.html')


def shop(request):
    return render(request, 'shop.html')


def shop_single(request):
    return render(request, 'shop-single.html')


def cart(request):
    return render(request, 'cart.html')


def contact(request):
    return render(request, 'contact.html')


def checkout(request):
    return render(request, 'checkout.html')


def thanks(request):
    return render(request, 'thankyou.html')

