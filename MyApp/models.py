from django.db import models

# Create your models here.

class Model_Claim_Data(models.Model):
    claim_numbers=models.CharField(max_length=100)
    resolutions=models.CharField(max_length=100)
