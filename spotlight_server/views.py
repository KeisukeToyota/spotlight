from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import csv
import json
from django.core import serializers

# Create your views here.


def index(request):
    return HttpResponse('hello')


def report(request):
    inputs = json.loads((request.body).decode('utf-8'))
    if len(serializers.serialize('json', Tweet.objects.filter(id=inputs['id']))) == 2:
        tweet = Tweet(id=inputs['id'],
                      user_id=inputs['user_id'],
                      retweet_count=inputs['retweet_count'],
                      favorite_count=inputs['favorite_count'],
                      in_reply_to_user_id=inputs['in_reply_to_user_id'],
                      in_reply_to_status_id=inputs['in_reply_to_status_id'],
                      text=inputs['text'],
                      created_at=inputs['created_at'],
                      iso_language_code=inputs['iso_language_code'],
                      source=inputs['source'],
                      lang=inputs['lang'],
                      good=0,
                      bad=0)
        tweet.save()
        if len(serializers.serialize('json', User.objects.filter(id=tweet.user_id))) == 2:
            user = User(id=tweet.user_id,
                        count=inputs['count'],
                        created_at=inputs['created_at'],
                        default_profile=inputs['default_profile'],
                        default_profile_image=inputs['default_profile_image'],
                        description=inputs['description'],
                        favorites_count=inputs['favorites_count'],
                        followers_count=inputs['followers_count'],
                        friends_count=inputs['friends_count'],
                        lang=inputs['lang'],
                        listed_count=inputs['listed_count'],
                        location=inputs['location'],
                        name=inputs['name'],
                        profile_background_image_url=inputs['profile_background_image_url'],
                        profile_image_url=inputs['profile_image_url'],
                        screen_name=inputs['screen_name'],
                        statuses_count=inputs['statuses_count'],
                        time_zone=inputs['time_zone'],
                        url=inputs['url'],
                        utc_offset=inputs['utc_offset'],
                        verified=inputs['verified'],
                        rank=0,
                        hash=inputs['hash'],)
            user.save()
        return HttpResponse(True)
    else:
        tweet = Tweet.objects.get(id=inputs['id'])
        if inputs['good'] == 1:
            tweet.good += inputs['good']
        elif inputs['bad'] == 1:
            tweet.bad += inputs['bad']
        if tweet.good <= tweet.bad:
            user = User.objects.get(id=tweet.user_id)
            user.rank = tweet.bad
        else:
            user = User.objects.get(id=tweet.user_id)
            user.rank = 0
        return HttpResponse(True)


def user_confirmation(request):
    inputs = request.GET
    print(len(serializers.serialize(
        'json', Infomation.objects.filter(id=inputs.get('id')))))
    if len(serializers.serialize('json', Infomation.objects.filter(id=inputs.get('id')))) != 2:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

# def user_index(request):


# def some_view(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
#
#     writer = csv.writer(response)
#     writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
#     writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
#
#     return response
