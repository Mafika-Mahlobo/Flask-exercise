from flask import Flask, render_template, request, escape
import vsearch

app = Flask(__name__)


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
    with open('vsearch.log', 'a') as logfile:
        print(req.form,  req.remote_addr, req.user_agent, res, file=logfile, sep='|')
    

@app.route('/viewlog')
def View_the_log() ->'html':
    
    content = []
    with open('vsearch.log') as log:
        for line in log:
            content.append([])
            for item in line.split('|'):
                content[-1].append(escape(item))
    titles = ('Form data','Remote_addr','User_agent','Results')
    return render_template(
        '/viewlog.html',
        the_title = 'View Log',
        the_row_tiles = titles,
        the_data = content
    )

if __name__ == '__main__':
    app.run(debug=True)


 