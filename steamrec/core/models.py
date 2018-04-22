from django.db import models


class Game(models.Model):
    appid = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    release_date = models.DateField(blank=True, null=True)
    header_image_url = models.URLField(blank=True, null=True)
    developer = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    metascore = models.IntegerField(blank=True, null=True)
    owners = models.IntegerField(blank=True, null=True)
    recent_review_count = models.IntegerField(blank=True, null=True)
    total_review_count = models.IntegerField(blank=True, null=True)
    recent_review_score = models.IntegerField(blank=True, null=True)
    total_review_score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name