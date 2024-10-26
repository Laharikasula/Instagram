from django.db import models

# Create your models here.
class instaPost(models.Model):
    person=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add="True")
    caption=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.caption
    
    
class plogin(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    
    def __str__(self):
        return self.username
    
