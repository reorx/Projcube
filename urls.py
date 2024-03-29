from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    (r'^$', views.v_home),
    (r'^accounts/login$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    (r'^accounts/logout$', 'accounts.logout'),
    (r'^accounts/signup$', 'accounts.signup'),
    #(r'^accounts/settings$', views.v_accounts_settings),

    (r'^context$', views.v_context),
)

urlpatterns += patterns('',
    (r'^user$', views.v_user),
    (r'^user/projs$', views.v_user_projs),
    (r'^user/tasks$', views.v_user_tasks),
)

urlpatterns += patterns('',
    (r'^projs$', views.v_projs),
    (r'^projs/create$', views.v_projs_create),
    (r'^projs/join$', views.v_projs_join),
    (r'^projs/(?P<id>\d+)$', views.v_projs_show),
    (r'^projs/(?P<id>\d+)/update$', views.v_projs_update),
    (r'^projs/(?P<id>\d+)/delete$', views.v_projs_delete),
    #(r'^projs/(?P<c>\w+)/settings$', views.v_projs_settings),
    (r'^projs/ajax$', views.v_projs_ajax),
    (r'^projs/ajax/show$', views.v_projs_ajax_show),
)

urlpatterns += patterns('',
    (r'^tasks$', views.v_tasks),
    (r'^tasks/ajax$', views.v_tasks_ajax),
    (r'^tasks/ajax/show$', views.v_tasks_ajax_show),
    (r'^tasks/ajax/create$', views.v_tasks_ajax_create),
    (r'^tasks/ajax/update$', views.v_tasks_ajax_update),
    (r'^tasks/ajax/delete$', views.v_tasks_ajax_delete),
    (r'^tasks/ajax/commenton$', views.v_tasks_ajax_commenton),
    (r'^tasks/ajax/done$', views.v_tasks_ajax_done),
    (r'^tasks/ajax/undone$', views.v_tasks_ajax_undone),
)

urlpatterns += patterns('',
    (r'^daysums$', views.v_daysums),
    #(r'^daysums/weekly$', views.v_daysums_weekly),
    #(r'^daysums/periodly$', views.v_daysums_periodly),
)

urlpatterns += patterns('',
    (r'^messages$', views.v_messages),
    #(r'^messages/sent$', views.v_messages_sent),
    #(r'^messages/received$', views.v_messages_received),
)

from django.contrib import admin
#admin.autodiscover()
from projcube import admin as models_admin
models_admin.autoregister()
urlpatterns += patterns('',
    (r'^admin/',include(admin.site.urls)),
)
