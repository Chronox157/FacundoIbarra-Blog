from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    fecha_add = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-fecha_add']
        
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    fecha_add = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['fecha_add']