
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('question/<int:pk>',views.test,name="index"),
    path('question/answer/<int:pk>',views.answer,name="answer"),
    path('question/xls',views.xsl,name='xls'),
    path('question/rand',views.do_rand,name='do'),


]
