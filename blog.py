import tornado.log
import tornado.ioloop
import tornado.web
from jinja2 import Environment, PackageLoader

ENV = Environment(
    loader=PackageLoader('blog', 'templates')
)

# Home Page Handler
class HomePageHandler(tornado.web.RequestHandler):

    def get(self):
        template = ENV.get_template('index.html')
        self.write(template.render())

# Make the Web Applicaton using Tornado
def make_app():
  return tornado.web.Application([
    (r"/", HomePageHandler),
    ], autoreload=True)

# Main
if __name__ == "__main__":

    tornado.log.enable_pretty_logging()

    app = make_app()
    app.listen(8888, print('Hosting at 8888'))
    tornado.ioloop.IOLoop.current().start()
