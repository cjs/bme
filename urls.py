from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.contrib import databrowse

from brc.models import *
from regionals.models import *

#from haystack.sites import SearchSite
#mysite = SearchSite()
#mysite.register(PlayaEvent)

#import haystack
#haystack.autodiscover()

#databrowse.site.register(Year)
#databrowse.site.register(CircularStreet)
#databrowse.site.register(TimeStreet)
#databrowse.site.register(ThemeCamp)
#databrowse.site.register(ArtInstallation)
#databrowse.site.register(PlayaEvent)
#databrowse.site.register(Vehicle)
#databrowse.site.register(TrackPoint)
#databrowse.site.register(ThreeDModel)

from account.openid_consumer import PinaxConsumer

import os.path

from microblogging.feeds import TweetFeedAll, TweetFeedUser, TweetFeedUserWithFriends
tweets_feed_dict = {"feed_dict": {
    'all': TweetFeedAll,
    'only': TweetFeedUser,
    'with_friends': TweetFeedUserWithFriends,
}}

from blog.feeds import BlogFeedAll, BlogFeedUser
blogs_feed_dict = {"feed_dict": {
    'all': BlogFeedAll,
    'only': BlogFeedUser,
}}

from bookmarks.feeds import BookmarkFeed
bookmarks_feed_dict = {"feed_dict": { '': BookmarkFeed }}

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {"template": "homepage.html"}, name="home"),
    url(r'^crossdomain.xml$', direct_to_template, {"template": "crossdomain.xml"}),

#    url(r'^playaevents/create$', 'brc.views.create_or_edit_event',
#		{'year_year':"2010"}, name="playa_event_edit"),
    url(r'^playaevents/create$', 'brc.views.create_or_edit_event',
                       direct_to_template, {"template": "disabled.html"},
                       name="playa_event_edit"),
    (r'^databrowse/(.*)', databrowse.site.root),
    (r'^about/', include('about.urls')),
    (r'^account/', include('account.urls')),
    (r'^openid/(.*)', PinaxConsumer()),
    (r'^bbauth/', include('bbauth.urls')),
#    (r'^authsub/', include('authsub.urls')),
    (r'^profiles/', include('profiles.urls')),
    (r'^blog/', include('blog.urls')),
    (r'^tags/', include('tag_app.urls')),
    (r'^invitations/', include('friends_app.urls')),
    (r'^notices/', include('notification.urls')),
    (r'^messages/', include('messages.urls')),
    (r'^announcements/', include('announcements.urls')),
    (r'^tweets/', include('microblogging.urls')),
    (r'^tribes/', include('tribes.urls')),
    (r'^regionals/', include('regionals.urls')),
    (r'^projects/', include('projects.urls')),
    (r'^comments/', include('threadedcomments.urls')),
    (r'^robots.txt$', include('robots.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^bookmarks/', include('bookmarks.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^photos/', include('photos.urls')),
    (r'^avatar/', include('avatar.urls')),
#   (r'^swaps/', include('swaps.urls')),
    (r'^flag/', include('flag.urls')),
    (r'^schedule/', include('schedule.urls')),
    (r'^playaevent/', include('swingtime.urls')),
    (r'^brc/', include('brc.urls')),
    (r'^api/docs/', 'brc.views.apidocs'),
    (r'^api/0.1/', include('api.urls')),
    (r'^feeds/tweets/(.*)/$', 'django.contrib.syndication.views.feed', tweets_feed_dict),
    (r'^feeds/posts/(.*)/$', 'django.contrib.syndication.views.feed', blogs_feed_dict),
    (r'^feeds/bookmarks/(.*)/?$', 'django.contrib.syndication.views.feed', bookmarks_feed_dict),
#	(r'^search/', include('haystack.urls')),

    (r'^points/', include('points.urls')),
    (r'^listings/', include('listings.urls')),
    (r'^checkins/', include('checkins.urls')),
)

## @@@ for now, we'll use friends_app to glue this stuff together

from photos.models import Photo

friends_photos_kwargs = {
    "template_name": "photos/friends_photos.html",
    "friends_objects_function": lambda users: Photo.objects.filter(member__in=users),
}

from blog.models import Post

friends_blogs_kwargs = {
    "template_name": "blog/friends_posts.html",
    "friends_objects_function": lambda users: Post.objects.filter(author__in=users),
}

from microblogging.models import Tweet

friends_tweets_kwargs = {
    "template_name": "microblogging/friends_tweets.html",
    "friends_objects_function": lambda users: Tweet.objects.filter(sender_id__in=[user.id for user in users], sender_type__name='user'),
}

from bookmarks.models import Bookmark

friends_bookmarks_kwargs = {
    "template_name": "bookmarks/friends_bookmarks.html",
    "friends_objects_function": lambda users: Bookmark.objects.filter(saved_instances__user__in=users),
    "extra_context": {
        "user_bookmarks": lambda request: Bookmark.objects.filter(saved_instances__user=request.user),
    },
}

urlpatterns += patterns('',
    url('^photos/friends_photos/$', 'friends_app.views.friends_objects', kwargs=friends_photos_kwargs, name="friends_photos"),
    url('^blog/friends_blogs/$', 'friends_app.views.friends_objects', kwargs=friends_blogs_kwargs, name="friends_blogs"),
    url('^tweets/friends_tweets/$', 'friends_app.views.friends_objects', kwargs=friends_tweets_kwargs, name="friends_tweets"),
    url('^bookmarks/friends_bookmarks/$', 'friends_app.views.friends_objects', kwargs=friends_bookmarks_kwargs, name="friends_bookmarks"),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'misc.views.serve')
    )
