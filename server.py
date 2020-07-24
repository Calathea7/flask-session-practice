from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    
    return render_template('form.html')

@app.route('/results')
def show_results():

    compliment = request.args.getlist("choosy")
    compliment = ", ".join(compliment)
    
    return render_template('results.html', compliment = compliment)

@app.route('/save-name')
def save_name():

    name = request.args.get("name")

    if 'name' in session:
        name = session['name'] 
    else:
        name = session['name'] = {}

    return redirect('http://0.0.0.0:5000/form')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
