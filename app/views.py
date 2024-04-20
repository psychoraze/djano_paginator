from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import Album
from django.views.generic import ListView, CreateView
from .forms import AlbumForm


def albums(request):
    albums = Album.objects.all()
    paginator = Paginator(albums, 3)
    if "page" in request.GET:
        page_num = request.GET["page"]
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    return render(request, "albums.html", {"page": page})


class AlbumList(ListView):
    model = Album
    template_name = "albums_class.html"
    context_object_name = "albums"
    paginate_by = 3


class CreateAlbum(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "create_album.html"
    success_url = reverse_lazy("albums_class")
