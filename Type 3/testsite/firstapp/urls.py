from django.conf.urls import url
from .views import home_view,login_veiw,logout_view,register_view
urlpatterns=[
    url(r'^$',home_view,name='home'),
    url(r'^login/$',login_veiw,name='login'),
    url(r'^logout/$',logout_view,name='logout'),
    url(r'^register/$',register_view,name='register')
]