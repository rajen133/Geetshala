
from django.urls import path,include
from songs import views

urlpatterns = [
    # path('songs/', include('songs.urls')),
    path('',views.song_list, name='song_list'),
    path('<int:song_id>/',views.song_detail, name='song_detail'),
]