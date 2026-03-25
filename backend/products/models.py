from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name="Nom")
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=350, verbose_name="Nom")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    stock = models.PositiveIntegerField(default=0, verbose_name="Quantité en stock")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
        verbose_name="Catégorie"
    )
    image = models.ImageField(null=True, blank=True, upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.name
