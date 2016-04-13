from django.conf.urls import include, url
from django.contrib import admin
from hello import views as hello_views
from accounts import views as accounts_views
# from accounts.views import register, profile, login, logout, cancel_subscription,subscriptions_webhook
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from product import views as product_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello_views.get_index, name='index'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^cancel_subscription/$', accounts_views.cancel_subscription, name='cancel_subscription'),
    url(r'^subscriptions_webhook/$', accounts_views.subscriptions_webhook, name='subscriptions_webhook'),
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return/$', paypal_views.paypal_return),
    url(r'^paypal-cancel/$', paypal_views.paypal_cancel),
    url(r'^product/$', product_views.all_products)
    # url(r'^pages/', include('django.contrib.flatpages.urls')),
]