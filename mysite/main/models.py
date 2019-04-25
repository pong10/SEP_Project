from django.db import models

# Create your models here.
class Tutorial(models.Model):
    tutorial_titile =models.CharField(max_length=200)
    tutorial_content=models.TextField()
    tutorial_published=models.DateTimeField("data published")
    def __str__(self):
        return self.tutorial_titile