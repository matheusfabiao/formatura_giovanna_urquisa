from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='guests/', blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True, max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Convidado'
        verbose_name_plural = 'Convidados'

    def __str__(self):
        """Return the string representation of the Guest object, which is the guest's name."""
        return self.name
