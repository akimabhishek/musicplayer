from django.contrib.auth import authenticate, login
from .models import Album,Song
from django.http import HttpResponse
from .forms import AlbumForm, SongForm, UserForm, LoginForm
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('Disabled A/C')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request,'music/login.html',{'form':form})

@login_required (login_url='/music/login/')
def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums':all_albums
    }
    return render(request, 'music/index.html',context)

@login_required (login_url='/music/login/')
def detail(request,album_id):
    if not request.user.is_authenticated:
        return render(request, 'music/login.html')
    else:
        user = request.user
        album = get_object_or_404(Album,pk=album_id)
        return render(request,'music/detail.html',{'album':album,'user':user})

@login_required (login_url='/music/login/')
def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'music/detail.html', {'album': album})

@login_required (login_url='/music/login/')
def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    album.delete()
    albums = Album.objects.filter(user=request.user)
    return render(request, 'music/index.html', {'albums': albums})

@login_required (login_url='/music/login/')
def create_album(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        form = AlbumForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            return render(request, 'music/detail.html', {'album': album})
        context = {
            "form": form,
        }
        return render(request, 'music/create_album.html', context)
@login_required (login_url='/music/login/')
def create_song(request, album_id):
    form = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        albums_songs = album.song_set.all()
        for s in albums_songs:
            if s.song_title == form.cleaned_data.get("song_title"):
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'music/create_song.html', context)
        song = form.save(commit=False)
        song.album = album
        song.save()
        return render(request, 'music/detail.html', {'album': album})
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'music/create_song.html', context)