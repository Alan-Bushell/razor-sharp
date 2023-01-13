from django.db import models

# Create your models here.


class Contact(models.Model):
    """Model for contact form"""
    CONTACT_CHOICES = [
        ('order', 'Order Tracking'),
        ('general', 'General Query'),
        ('complaint', 'Complaint'),
        ('return', 'Return Request'),
    ]
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=700)
    reason = models.CharField(max_length=15, choices=CONTACT_CHOICES)

    def __str__(self):
        return self.email
