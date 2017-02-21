from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100, blank=True)
    video_id = models.CharField(max_length=100, blank=True)
    ch_id = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
