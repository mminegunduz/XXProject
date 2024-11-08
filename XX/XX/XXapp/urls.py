from . import views
from django.urls import path

app_name='XXapp'


urlpatterns = [
    path('anasayfa/', views.anasayfa, name='anasayfa'),#...com/XXapp/anasayfa
    path('gonderiekle/', views.gonderiekle, name='gonderiekle'), #...com/XXapp/gonderiekle
    path('', views.giris, name='giris'), #giris sayfasi direkt buraya atanacak ...com/XXapp/
    path('hakkinda/', views.hakkinda, name='hakkinda') #...com/XXapp/hakkinda
]
