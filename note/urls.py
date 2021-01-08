from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list', views.list),
    url(r'^add', views.add),
    url(r'^mod/(\d+)', views.mod),
    url(r'^del/(\d+)', views.delete),
]
