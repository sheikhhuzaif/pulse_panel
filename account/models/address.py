from django.db import models

class Address(models.Model):
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.address+" "+self.city