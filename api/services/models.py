from django.db import models

from api.post.models import Post
from api.account.models import User

# Create your models here.

class ReactionManager(models.Manager):

    def likes(self):
        return self.get_queryset().filter(reaction__gt=0).count()
    def dislikes(self):
        return self.get_queryset().filter(reaction__lt=0).count()

class Reaction(models.Model):

    REACTION = (
        ('1', 'LIKE'),
        ('-1', 'DISLIKE'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_reactions")
    reaction = models.IntegerField(choices=REACTION,help_text="1=LIKE,-1=DISLIKE",null=True)

    objects = ReactionManager()

    class Meta:
        unique_together = ["user", "post", "reaction"]

    def __str__(self):
        return (f"{self.user.email} reacted on {self.post.title} with a {self.reaction}")
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()

    def __str__(self):
        return f"{self.user} commented on {self.post}"