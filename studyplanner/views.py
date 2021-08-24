from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic import View
from .models import Album, Song
from .forms import UserForm

# Create your views here.

#views contain functions or urls that are mapped to urls

def index(request):
    all_albums=Album.objects.all()
    template=loader.get_template('studyplanner/index.html')
    context= {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context,request))
    '''
    html=''
    all_albums=Album.objects.all()
    for album in all_albums:
        url='/studyplanner/'+str(album.id) +'/'
        html+='Welcome to Kushal Shah - Time Table<br><br><a href='+url+'> '+ str(album.album_title) +'</a><br>'
    return HttpResponse(html)
    '''
def detail(request,album_id):
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'studyplanner/detail.html', {'album':album})

    #return HttpResponse("<h2>Details for Album Id "+str(album_id)+ "</h2>")

def favourite(request,album_id):
    album= get_object_or_404(Album, pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request,'studyplanner/detail.html',{
            'album': album,
            'error_message':"You did not select a valid song",
        })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        #print(selected_song.isFavourite + " "+ selected_song.song_title)
        return render(request, 'studyplanner/detail.html', {'album':album})




def monday(request):
    return HttpResponse("Monday's Time Table is - Nothing")
def tuesday(request):
    return HttpResponse("Tuesday time table is - Nothing")

def weekly_timetable(request,day):
    text=""
    if (day=='monday'):
        text="It is Monday"
    elif (day=='tuesday'):
        text="It si Tuesday"
    return HttpResponse(text) 


# generic views
class IndexView(generic.ListView):
    template_name='studyplanner/index.html'
    context_object_name='all_albums'
    def get_queryset(self):
        return Album.objects.all()
    

class AlbumCreate(CreateView):
    model=Album
    template_name='studyplanner/album_form.html'
    fields=['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model=Album
    success_url=reverse_lazy('studyplanner:index')

class UserFormView(View):
    form_class=UserForm
    template_name='studyplanner/registration_form.html'
    
    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form': form})
    
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid:
            #cleaned normalised data
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return user object after authentication if details are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('studyplanner:index')
        
        return render(request, self.template_name,{'form': form})




    
