from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "User %s  %s %s" % (self.id, self.name, self.email)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"