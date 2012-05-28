import sys
import cherrypy
from cherrypy.process.plugins import Daemonizer
Daemonizer(cherrypy.engine).subscribe()
from pygments                 import highlight
from pygments.lexers          import get_lexer_by_name
from pygments.formatters      import HtmlFormatter

class Root:
  def pygments(self, lang, code):
    lexer     = get_lexer_by_name(lang)
    formatter = HtmlFormatter()
    return highlight(code, lexer, formatter)
  pygments.exposed = True

config = {'global': {'server.socket_host': '0.0.0.0', 'server.socket_port': int(sys.argv[1])}}
cherrypy.quickstart(Root(), config=config)
