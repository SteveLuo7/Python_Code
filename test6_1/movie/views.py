from django.shortcuts import render

from movie.models import Movies


# Create your views here.
def index_view(request):
    #   enquire all the information
    movieList = Movies.objects.all()

    return render(request,'index01.html',{'movieList':movieList})