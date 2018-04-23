from django.db import models


class Game(models.Model):
    appid = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    app_type = models.ForeignKey(AppType)
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
    date_added = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.name


class AppType(models.Model):
    name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)


class Tag(models.Model):
    name = models.CharField(max_length=128)


class GameTag(models.Model):
    game = models.ForeignKey(Game)
    tag = models.ForeignKey(Tag)
