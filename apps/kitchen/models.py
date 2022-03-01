from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 244)
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveBigIntegerField()


    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length = 244)
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name

    # def self_price(self):
    #     return self.quantity.weight.quantity % 1000 % self.quantity.product.price

class Weight(models.Model):
    weight = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete = models.CASCADE, related_name = 'weight')

    def __str__(self):
        return (f"{self.meal}'s {self.product}")

    def price(self):
        return 1000 / self.weight / self.product.price

    class Meta:
        verbose_name_plural = "quantities"


