from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="events")

    class Meta:
        ordering = ('-created',)
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title
