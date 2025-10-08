from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    time = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100, null=False)
    emoji_reactions = models.JSONField(default=dict)  # e.g. {"👍": 3, "⭐": 1}
    
    def __str__(self):
        return self.title
