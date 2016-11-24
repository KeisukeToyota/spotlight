from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import csv
import json
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    return render(request, 'index.html')


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
                        profile_background_image_url=inputs[
                            'profile_background_image_url'],
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
        if inputs['safe'] is True:
            tweet.good += inputs['good']
        else:
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
    if len(serializers.serialize('json', Infomation.objects.filter(id=inputs.get('id')))) != 2:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def version_check(request):
    return json.dumps({'version': '0.2.1'})


def tweet_index(request):
    inputs = request.GET
    tweet_list = Tweet.objects.filter(user_id=inputs.get('id'))
    paginator = Paginator(tweet_list, 25)
    page = request.GET.get('page')
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)
    d = {
        'tweets': tweets,
        'id': inputs.get('id')
    }
    return render(request, 'tweet.html', d)


def user_index(request):
    user_list = User.objects.all()
    paginator = Paginator(user_list, 25)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    d = {
        'users': users,
    }
    return render(request, 'user.html', d)


def user_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID',
                     'Screen name',
                     'Name',
                     'Followers count',
                     'Friends count',
                     'Location',
                     'Description',
                     'Profile image',
                     'Rank',
                     'Created at'])
    user_list = User.objects.all()
    paginator = Paginator(user_list, 25)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    for user in users:
        writer.writerow([user.id,
                         user.screen_name,
                         user.name,
                         user.followers_count,
                         user.friends_count,
                         user.location,
                         user.description,
                         user.profile_image_url,
                         user.rank,
                         user.created_at])

    return response


def tweet_csv(request):
    inputs = request.GET
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID',
                     'Retweet count',
                     'Favorite count',
                     'Text',
                     'Created at',
                     'Good',
                     'Bad'])
    tweet_list = Tweet.objects.filter(user_id=inputs.get('id'))
    paginator = Paginator(tweet_list, 25)
    page = request.GET.get('page')
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)
    for tweet in tweets:
        writer.writerow([tweet.id,
                         tweet.retweet_count,
                         tweet.favorite_count,
                         tweet.text,
                         tweet.created_at,
                         tweet.good,
                         tweet.bad])

    return response
