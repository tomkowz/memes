from django.http import HttpResponse, Http404
from index_renderer import IndexRenderer
from memes import Memes, Meme

import os.path
import re

def index(request):
    baseDir = os.path.abspath(os.path.dirname(__file__))
    memes = Memes.load(baseDir)
    response = IndexRenderer(memes).render()
    return HttpResponse(response) 

def get_meme(request):
    # Find a match
    id = request.path.rsplit('/', 1)[-1]

    # Load memes
    baseDir = os.path.abspath(os.path.dirname(__file__))
    memes = Memes.load(baseDir)

    for meme in memes:
        if meme.id == id:
            binary = file(meme.filepath, 'rb').read()
            contentType = _get_meme_content_type(meme.filepath)
            response = HttpResponse(binary, content_type=contentType)
            return response 

    raise Http404
    
def _get_meme_content_type(filename):
    contentTypes = {
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif'
    }

    extensionLocation = filename.rfind('.') + 1
    extension = filename[extensionLocation:].lower()

    return contentTypes[extension]
