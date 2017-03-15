#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


    def post(self):
        skrivno_stevilo = 42
        ugani_stevilo = int(self.request.get("ugani_stevilo"))

        rezultat = []

        while True:
            if ugani_stevilo == skrivno_stevilo:
                rezultat = "BRAVO USPELO TI JE!"
            elif ugani_stevilo > skrivno_stevilo:
                rezultat = "Nizje, ugani stevilo se enkrat!"
            else:
                rezultat = "Visje, ugani stevilo se enkrat!"

            spremenljivke = {"rezultat": rezultat}

            return self.render_template("rezultat.html", spremenljivke)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
