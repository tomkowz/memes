class IndexRenderer(object):

    def __init__(self, memes):
        self.memes = memes

    def render(self):
        # Begin document
        response = '<html>'

        # HEAD
        response += '<head>'

        response += """
        <style media="screen" type="text/css">
            a {
                font-size: 14px;
                text-decoration: none;
                margin-right: 15px;
                line-height: 30px;
                color: #1daa55;
            }

            a:hover {
                text-decoration: underline;
            }
        </style>
        """

        response += '</head>'

        # BODY
        response += '<body>'
        response += self._render_list()
        response += '</body>'

        # End document
        response += '</html>'
        
        return response

    def _render_list(self):
        output = ''
        for meme in self.memes:
            output += '<a href="{}">{}</a>'.format(meme.url, meme.id)

        return output