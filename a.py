import web

urls=(
    '/','first',
    '/second','second'
)
render=web.template.render('templates')

class first:
    def GET(self):
        return render.first()
    def POST(self):
        return web.redirect("http://www.baidu.com")
    
    
if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()

