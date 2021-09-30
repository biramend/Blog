from django.db import models
from uuid import uuid4

# Create your models here.
def picture_image(instance,filename):
    extension = filename.split('.')[-1]
    return 'static/images/{}.{}'.format(uuid4().hex, extension)
    

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    slug = models.SlugField(max_length=200)
    date_pub = models.DateTimeField(auto_now_add=True)
    imae = models.FileField(upload_to=picture_image,null=True)


    def __str__(self):
        return self.titre