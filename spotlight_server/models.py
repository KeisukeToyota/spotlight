from django.db import models

# Create your models here.


class Report(models.Model):
    id = models.IntegerField(
        primary_key=True, max_length=11, unique=True, auto_created=True)
    name = models.CharField(max_length=255, null=True)
    comment = models.TextField(null=True)
    os = models.CharField(max_length=255, null=True)
    pcuser = models.CharField(max_length=255, null=True)
    ip = models.CharField(max_length=255, null=True)
    date = models.CharField(max_length=255, null=True)
    macaddress = models.CharField(max_length=255, null=True)
    hash = models.CharField(max_length=255, null=True)


class Infomation(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, null=True)
    accesstoken = models.CharField(max_length=255, null=True)
    organization = models.CharField(max_length=255, null=True)
    date = models.CharField(max_length=255, null=True)


class User(models.Model):
    count = models.IntegerField(
        primary_key=True, max_length=11, auto_created=True)
    created_at = models.CharField(max_length=255, null=True)
    default_profile = models.CharField(max_length=255, null=True)
    default_profile_image = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    favorites_count = models.CharField(max_length=255, null=True)
    followers_count = models.CharField(max_length=255, null=True)
    friends_count = models.CharField(max_length=255, null=True)
    id = models.CharField(max_length=255, null=True)
    lang = models.CharField(max_length=255, null=True)
    listed_count = models.CharField(max_length=255, null=True)
    location = models.TextField(null=True)
    name = models.TextField(null=True)
    profile_background_image_url = models.TextField(null=True)
    profile_image_url = models.TextField(null=True)
    screen_name = models.TextField(null=True)
    statuses_count = models.CharField(max_length=255, null=True)
    time_zone = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    utc_offset = models.CharField(max_length=255, null=True)
    verified = models.CharField(max_length=255, null=True)
    rank = models.IntegerField(max_length=11, null=True)
    hash = models.CharField(max_length=255, null=True)


class Tweet(models.Model):
    retweet_count = models.CharField(max_length=255, null=True)
    favorite_count = models.CharField(max_length=255, null=True)
    in_reply_to_user_id = models.CharField(max_length=255, null=True)
    in_reply_to_status_id = models.CharField(max_length=255, null=True)
    text = models.CharField(max_length=255, null=True)
    id = models.CharField(max_length=255, primary_key=True)
    created_at = models.CharField(max_length=255, null=True)
    iso_language_code = models.CharField(max_length=255, null=True)
    source = models.CharField(max_length=255, null=True)
    lang = models.CharField(max_length=255, null=True)
    good = models.IntegerField(max_length=11, null=True)
    bad = models.IntegerField(max_length=11, null=True)
    user_id = models.CharField(max_length=255, null=True)
