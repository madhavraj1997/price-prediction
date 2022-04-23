# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User,  on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username

# class Portfolio(models.Model):
#     company_name = models.CharField(max_length=100)
#     current_unit = models.IntegerField()
#     sold_unit = models.IntegerField()
#     Investment = models.FloatField()
#     current_value = models.FloatField()
#     receivable_amount = models.FloatField()

#     def __str__(self):
#         return self.company_name


# class Watchlist(models.Model):
#     serial_number = models.IntegerField()
#     company_name = models.CharField(max_length=100)
#     high_price = models.FloatField()
#     low_price = models.FloatField()
#     volume = models.FloatField()
#     prev_closing = models.FloatField()


#     def __str__(self):
#         return self.serial_number




