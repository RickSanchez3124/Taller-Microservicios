from django.db import models

class Place(models.Model):
    variable = models.IntegerField(null=False, default=None)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.name)
