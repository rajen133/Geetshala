from django.shortcuts import render

# Create your views here.
from os import name
from django.http import HttpResponse

def song_list(request):
    songs=[
        {'id':1, 'title':'Broken Angle'},
        {'id':2, 'title':'One night in Dubai'},
        {'id':3, 'title':'Chikiri Chikiri'},
        {'id':4, 'title':'Bohemian Rhapsody'},
        {'id':5, 'title':'Stairway to Heaven'},
        {'id':6, 'title':'Smells Like Teen Spirit'},
        {'id':7, 'title':'Imagine'},
        {'id':8, 'title':'Lose Yourself '},
        {'id':9, 'title':'Baby Baby'},
        {'id':10, 'title':'Broken Angle'},
    ]
    return render(request,'songs/song_list.html',{'songs':songs})

def song_detail(request, song_id):
    return render(request, 'songs/song_detail.html', {'song_id':song_id, 'song_name':'Sample Song'})