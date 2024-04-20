from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "cover", "author", "description", "price"]
        help_texts = {
            "title": "Enter Album Title",
            "cover": "Album's Cover",
            "author": "Album's Author",
            "description": "Album's Description",
            "price": "Vinyl price",
        }
        labels = {
            "title": "Title",
            "cover": "Cover",
            "author": "Author",
            "description": "Description",
            "price": "Price",
        }
