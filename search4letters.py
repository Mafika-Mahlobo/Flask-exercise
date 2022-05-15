from flask import Flask, render_template, request, escape, session
import vsearch
from DBcm import UseDatabase
from checker import check_logged_in

app = Flask(__name__)

app.secret_key = 'ThisIsSearchForLettersKey'

@app.route('/login')
def login()->str:
	session['logged_in'] = True
	return 'You are now logged in'

@app.route('/logout')
def logout()->str:
	session.pop('logged_in')
	return 'You are now logged out'


app.config['dbconfig'] = {'host' : '127.0.0.1', 'user' : 'vsearch', 'password' : 'vsearchpasswd', 'database' : 'vsearchlogDB',}

@app.route('/search4',methods=['POST'])
def do_search()->'html':

    phrase = request.form['phrase']
    letters = request.form['letters']
    result = str(vsearch.search4letter(phrase,letters))
    log_request(request, result)
    return render_template('/results.html',the_phrase=phrase,
     the_letters=letters,
     the_results=result,
     the_title='Here are your results: ')

@app.route('/')
@app.route('/entry')
def entry_page() ->'html':
    return render_template('/entry.html',the_title='Welcome to search4letters on the web!')


def log_request(req: 'flask_request', res: str) ->None: 

    with UseDatabase(app.config['dbconfig']) as cursor:
    	_SQL = """INSERT INTO log (phrase, letters, ip, browser_string, results) VALUES (%s, %s, %s, %s ,%s)"""
    	cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res,))

    
@app.route('/viewlog')
@check_logged_in
def View_the_log() ->'html':
    
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ('phrase', 'letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template(
        '/viewlog.html',
        the_title = 'View Log',
        the_row_tiles = titles,
        the_data = contents
    )

if __name__ == '__main__':
    app.run(debug=True)


 