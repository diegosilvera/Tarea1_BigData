from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('literalA', views.literalA, name='literalA'),
    path('literalB', views.literalB, name='literalB'),
    path('literalC', views.literalC, name='literalC'),
    path('literalD',views.literalD,name='conteo'),
    path('literalE', views.literalE, name='literalE'),
    path('literalF', views.literalF, name='literalF'),
]
