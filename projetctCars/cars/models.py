from django.db import models

#nome da classe no banco de dados

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,related_name="car_brand",)
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    plate = models.CharField(max_length=20,blank=True,null=True)
    value = models.FloatField(blank=True,null=True)
    photo = models.ImageField(upload_to='cars/',blank=True,null=True) #precisa ajustar os arquivos estáticos.

    def __str__(self):
        return self.model

