from django.db import models

class Contact(models.Model):
    username = models.CharField(max_length=122)
    course = models.CharField(max_length=122, default="unknown")
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=100)  # Adjust as needed

    def __str__(self):
        return self.username

    class Meta:
        db_table = "contact"
