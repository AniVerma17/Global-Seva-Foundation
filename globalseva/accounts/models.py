from django.db import models

# Create your models here.
class NGO(models.Model):
	darpanId = models.CharField(max_length = 30, default = "")
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 50)
	name = models.CharField(max_length = 20)
	mail = models.CharField(max_length = 20)
	address = models.CharField(max_length = 50)
	phoneno = models.BigIntegerField()
	orgLogo = models.ImageField(upload_to = 'ngologos')
	certificate = models.ImageField(upload_to = 'ngocerts')
	rating = models.DecimalField(max_digits = 3, decimal_places = 2)

	class Meta:
		db_table = "ngos"


class Civilian(models.Model):
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 50)
	name = models.CharField(max_length = 20)
	mail = models.CharField(max_length = 20)
	address = models.CharField(max_length = 50)
	phoneno = models.BigIntegerField()
	profilePic = models.ImageField(upload_to = 'userdps')

	class Meta:
		db_table = "civilians"


class Basket(models.Model):
	posted_by = models.ForeignKey(Civilian, on_delete = models.CASCADE)
	claimed_by = models.ForeignKey(NGO, null = True, on_delete = models.SET_NULL)
	claimed = models.BooleanField(default = False)
	itemCount = models.IntegerField()
	itemDesc = models.CharField(max_length = 100)
	basketPic = models.ImageField(upload_to = 'basketpics')

	class Meta:
		db_table = "baskets"

	def isClaimed(self):
		return self.claimed