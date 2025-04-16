from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE =   [
        ('ML', 'MASALA'),
        ('PL', 'PLAIN'),
        ('OL', 'OOLONG'),
        ('EL', 'ELICHI'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
    ]

    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)

    def __str__(self):
        return self.name
    

# one to many relation

class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name="review")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review on the {self.chai.name}"
    
# Many to many 

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(ChaiVarity, related_name='stores')

    def __str__(self):
        return self.name

# One to one 

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=50)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.name.chai}"
    

