from flask import Flask, render_template
app = Flask (__name__)

@app.route ('/')
def home ():
	return render_template ('template.html')
	
@app . route ('/ force404 ')
def force404 ():
	abort (404)

@app . errorhandler (404)
def page_not_found ( error ):
	return render_template ('error.html')

@app.route ('/kids')
def kids ():
	return render_template ('kids.html')
	
@app.route ('/kids/shoes')
def kidsshoes ():
	return render_template ('kidsshoes.html')
	
@app.route ('/kids/trousers')
def kidstrousers ():
	return render_template ('kidstrousers.html')
	
@app.route ('/kids/tops')
def kidstops ():
	return render_template ('kidstops.html')

@app.route ('/men')
def men ():
	return render_template ('men.html')
	
@app.route ('/men/shoes')
def menshoes ():
	return render_template ('menshoes.html')
	
@app.route ('/men/trousers')
def mentrousers ():
	return render_template ('mentrousers.html')
	
@app.route ('/men/tops')
def mentops ():
	return render_template ('mentops.html')
	
@app.route ('/women')
def women ():
	return render_template ('women.html')
	
@app.route ('/women/tops')
def womentops ():
	return render_template ('womentops.html')
	
@app.route ('/women/trousers')
def womentrousers ():
	return render_template ('womentrousers.html')
	
@app.route ('/women/shoes')
def womenshoes ():
	return render_template ('womenshoes.html')

if __name__ == (" __main__ "):
 app.run( host ='0.0.0.0 ', debug = True )
