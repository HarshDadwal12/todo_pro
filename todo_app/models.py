from django.db import models

# Create your models here.
class List(models.Model):
    item=models.CharField(max_length=100)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.item + '|' + str(self.status)
