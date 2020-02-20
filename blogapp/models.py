from django.db import models
from  django.utils import timezone
from django.conf import settings

# Create your models here.
#class name is table name e.g Post is a table name
class Post(models.Model):    
    # the assigned variables are the attributes
    #cascade is used to delete every item attached to an attribute
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title