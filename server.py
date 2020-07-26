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

@app.route('/save-name', methods=['POST', 'GET'])
def save_name():

    if request.method == 'POST':
        name = request.form['name']
        session["name"] = name
        return redirect('/form')
    else:
        return render_template("homepage.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
