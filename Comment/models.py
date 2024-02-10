from django.db import models
from Post.models import Articles
# Create your models here.
class Comment(models.Model):
   name=models.CharField(max_length=50,default="ناشناس")
   email=models.EmailField(max_length=50,blank=False,null=True)
   message=models.TextField(null=False,blank=False)
   post = models.ForeignKey(Articles,
                            on_delete=models.CASCADE,
                            related_name='comments')
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   active = models.BooleanField(default=True)
   class Meta:
      ordering = ('created',)

   def __str__(self):
      return 'Comment by {} on {}'.format(self.name, self.post)