from bottle import Bottle, redirect, run, \
     template, debug, get, route, static_file, request, post
import sqlite3 as lite
import os, sys

dirname = os.path.dirname(sys.argv[0])

#povezivanje baze
con=lite.connect('baza\\kviz3.db')
cur =con.cursor()
save_id=0

app = Bottle()
debug(True)

@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

@app.route('/static/<filename:re:.*\.jpg>')
def send_css(filename):
    return static_file(filename, root=dirname+'/static/assets/icons')

@app.route('/static/<filename:re:.*\.css.map>')
def send_cssmap(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root=dirname+'/static/assets/js')

@app.route('/static/<filename:re:.*\.js.map>')
def send_jsmap(filename):
    return static_file(filename, root=dirname+'/static/assets/js')

@app.route('/adminSignIn',method=['GET','POST'])
def adminSignIn():
    if request.POST.get('kliklog','').strip():
        username=request.POST.get('username')
        sifra=request.POST.get('password')
        cur.execute('SELECT * FROM admin WHERE ime=? AND sifra=?',(username,sifra))
        id1=cur.fetchone()
        if id1!=None:
            redirect('/pitanja')
        else:
            return template('Admin_logiranje')
    else:
        return template('Admin_logiranje')


@app.route('/igra')
def Igra():  
    pitanja=cur.execute("SELECT * FROM pitanja")
    return template('PT_Pocetak', pitanja=pitanja)

@app.route("/about")
def About():
    return template("About_")

@app.route("/poraz")
def About():
    return template("Poraz")

@app.route("/pobjeda")
def About():
    return template("Pobjeda")


@app.route('/delete<delete:re:[0-9]+>')
def brisanje(delete):
    br=delete
    cur.execute('DELETE FROM pitanja WHERE id = (?)',(br,))
    con.commit()
    redirect('/pitanja')

@app.route("/login")
def do_login():
    return template("Admin_logiranje")

@app.route("/")
def poc():
    redirect("/naslovna")

@app.route('/pitanja')
def popisPitanja():
    rows=cur.execute('SELECT * FROM pitanja')
    return template("Admin_dodavanje",rows=rows)



@app.route('/novo',method=['GET','POST'])
def popisPitanja():
    if request.POST.get('spremi','').strip():
        pitanje=request.POST.get('pitanje')
        broj=request.POST.get("brpit")
        odgA=request.POST.get('odgA')
        odgB=request.POST.get('odgB')
        odgC=request.POST.get('odgC')
        odgD=request.POST.get('odgD')
        tocan=request.POST.get('tocanOdg')
        cur.execute('INSERT INTO pitanja VALUES(null,?,?,?,?,?,?,?)',(broj,pitanje,odgA,odgB,odgC,odgD,tocan))
        con.commit()  
        redirect('/pitanja')
    return template('novoPitanje')

@app.route('/uredivanje<uredivanje:re:[0-9]+>', method=['GET','POST'])
def uredivanje(uredivanje):
    uredenoPitanje=uredivanje
    sys.stderr.write("Piranje: " + uredenoPitanje)
##    global save_id
##    if save_id==0:
##        redirect('/') #IF WE WERE ON ROUTE '/uredivanje' AND WE STOP THE SERVER AND START IT AGAIN, THEN REFRESH '/new' IT WILL REDIRECT US TO '/'
    if request.POST.get('spremi','').strip():
        broj=request.POST.get('brpit')
        pitanje = request.POST.get('pitanje')
        odgA = request.POST.get('odgA')
        odgB = request.POST.get('odgB')
        odgC = request.POST.get('odgC')
        odgD = request.POST.get('odgD')
        tocan = request.POST.get('tocanOdg')
        cur.execute('UPDATE pitanja SET broj=(?),pitanje=(?),odgovorA=(?),odgovorB=(?),odgovorC=(?),odgovorD=(?),tocanOdg=(?) WHERE id=(?)',(broj,pitanje,odgA,odgB,odgC,odgD,tocan,uredenoPitanje,))
        con.commit()
        redirect('/pitanja')
    else:
        #DATABASE QUERY
        rows=cur.execute('SELECT * FROM pitanja WHERE id=(?)',(uredenoPitanje,))    
        rezultat=cur.fetchone()
        
        save_id=rezultat[0]
        broj=rezultat[1]
        pitanje=rezultat[2]
        odgA=rezultat[3]
        odgB=rezultat[4]
        odgC=rezultat[5]
        odgD=rezultat[6]
        tocan=rezultat[7]
        return template('uredivanje',broj=broj,pitanje=pitanje,odgA=odgA,odgB=odgB,odgC=odgC,odgD=odgD,tocan=tocan,uredenoPitanje=uredenoPitanje)

@app.route('/')
def title():
    global save_id
    save_id=0
    print("Initialized save_id:")
    print(save_id)
    return template('PT_Naslovna')

run(app, host='localhost', port = 1236, debug='True', reloader='True')
