from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='название категории')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='описание категории')
    image = models.ImageField(verbose_name='картинка категории', upload_to='images/category/%Y/%m/%d')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='название продукта')
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='описание товара')
    price = models.FloatField(verbose_name='цена товара')
    image = models.ImageField(verbose_name='картинка товара', upload_to='images/product/%Y/%m/%d')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
