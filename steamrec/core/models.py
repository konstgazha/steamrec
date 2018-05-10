from django.db import models


class AppType(models.Model):
    name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)


class Game(models.Model):
    appid = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    app_type = models.ForeignKey(AppType, on_delete=models.CASCADE)
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


class Tag(models.Model):
    name = models.CharField(max_length=128)


class GameTag(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Player(models.Model):
    steamid = models.CharField(max_length=128, unique=True)
    game_count = models.IntegerField(blank=True, null=True)
    public = models.BooleanField(default=True)
    avatar = models.CharField(max_length=128)
    avatarmedium = models.CharField(max_length=128)
    avatarfull = models.CharField(max_length=128)
    date_added = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return str(self.steamid)