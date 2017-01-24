from django.http import HttpResponse, Http404
from index_renderer import IndexRenderer
from memes import Memes, Meme

import json
import os.path
import re

def index(request):
    baseDir = os.path.abspath(os.path.dirname(__file__))
    memes = Memes.load(baseDir)
    response = IndexRenderer(memes).render()
    return HttpResponse(response) 

def get_meme(request):
    # Find a match
    filename = request.path.rsplit('/', 1)[-1]

    # Load memes
    baseDir = os.path.abspath(os.path.dirname(__file__))
    memes = Memes.load(baseDir)

    for meme in memes:
        if meme.filename == filename:
            binary = file(meme.filepath, 'rb').read()
            contentType = _get_meme_content_type(filename)
            response = HttpResponse(binary, content_type=contentType)
            return response 

    raise Http404

def api_get_memes(request):
    baseDir = os.path.abspath(os.path.dirname(__file__))
    memes = Memes.load(baseDir)
    
    jsonMemes = []
    for meme in memes:
        memeJSON = meme.toJSON()
        del memeJSON["id"]
        del memeJSON["filepath"]
        jsonMemes.append(memeJSON)

    response = {"memes": jsonMemes}

    return HttpResponse(json.dumps(response), content_type="application/json")
    
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
