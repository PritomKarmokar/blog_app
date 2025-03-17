from django.db import models

"""
class Post:
    id int
    title str(50)
    content text
    created_at datetime
"""

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
