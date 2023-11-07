from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'))
    price = models.FloatField(verbose_name=_('price'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('author'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='pics', blank=True, null=True, verbose_name=_("image"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"))


class ShoppingCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    upload_at = models.DateTimeField(auto_now_add=True, verbose_name=_("upload_at"))
    count = models.IntegerField(default=1, verbose_name=_("count"))

    def __str__(self):
        return f'{self.product.name} from {self.user.username}'


class Comment(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    STATUS = (
        (1, 'Created'),
        (2, 'Wait for payment'),
        (3, 'Paid'),
        (4, 'Delivering'),
        (5, 'Completed')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS)

    def __str__(self):
        return f'{self.service.title} >>>> {self.status}'
