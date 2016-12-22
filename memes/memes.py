from os import listdir
from os.path import isfile, join

import json
import os

class Meme(object):

    def __init__(self, id, filename, filepath):
        self.id = id
        self.filename = filename
        self.filepath = filepath

class Memes(object):

    @staticmethod
    def load(baseDir):
        resourcesDir = baseDir + '/resources'
        
        # Filter files
        files = [f for f in listdir(resourcesDir) if isfile(join(resourcesDir, f))]
        supportedExtensions = ('.jpg', '.jpeg', '.png', '.gif')
        files = [f for f in files if f.endswith(supportedExtensions)]

        memes = []
        for f in files:
            dotLocation = f.rfind('.')

            id = f[:dotLocation]
            filepath = resourcesDir + '/' + f

            meme = Meme(id, f, filepath)
            memes.append(meme)

        return memes
