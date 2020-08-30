from django.db import models
from django.conf import settings
from .managers import ProductManager

CURRENCY = settings.CURRENCY


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=150, unique=True)
    Category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    value = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    discount_value = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    final_value = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    qty = models.PositiveIntegerField(default=0)

    # https://docs.djangoproject.com/en/2.0/topics/db/managers/
    # we can override Managers base query set
    # this model has two managers default(objects) and browser
    # objects will return all Products while browser will return only products that are active and have some qty
    objects = models.Manager()
    browser = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        self.final_value = self.discount_value if self.discount_value > 0 else self.value
        super.save(*args, **kwargs)

    def __str__(self):
        return self.title

    def tag_final_value(self):
        return f'{self.final_value} {CURRENCY}'

    tag_final_value.short_description = 'Value'
