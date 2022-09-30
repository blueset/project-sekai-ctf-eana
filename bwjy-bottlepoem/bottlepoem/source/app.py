from bottle import route, run, template,request,response,error
from config.secret import sekai
import os
import re
@route("/")
def home():
    return template('index')
@route("/show")
def index():
    param = request.query.id
    if(re.search('^../app',param)):
        return "No!!!!"
    requested_path = os.path.join(os.getcwd()+'/poems',param)
    try:
        with open(requested_path) as f:
            tfile = f.read()
    except Exception as e:
        return "No This Poems"
    response.set_header('Content-Type', 'text/plain')
    return tfile

@error(404)
def error404(error):
    return template('error')
@route("/sign")
def index():
    session = request.get_cookie('name',secret=sekai)
    if(not session or session['name']=="guest"):
        session={"name":"guest"}
        response.set_cookie('name',session,secret=sekai)
        return template('guest',name=session['name'])
    if(session['name'] == "admin"):
        return template('admin',name=session['name'])

if __name__ == '__main__':
    run(host='0.0.0.0', port=80)