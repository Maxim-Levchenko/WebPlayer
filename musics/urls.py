from django.urls import path
from musics import views

app_name = 'musics'

urlpatterns = [
    path('albums/', views.albums, name='albums'),
    path('albums/<int:album_id>', views.album, name='albums_page'),
]