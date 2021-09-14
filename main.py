from flask import Flask, render_template, redirect, url_for, request
import csv

app = Flask(__name__)


# print (__name__)

@app.route("/")
def index_main():
    # return "<p>Hello, Saurabh!!!! </p>"
    return render_template("index.html")


@app.route("/<string:page>")
def html_page(page):
    return render_template(page)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thank_you.html')
    else:
        return "something went wrong try again"


def write_to_csv():
    with open("database.csv", newline="", mode="a") as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(database, delimiter=',',
                              quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow(email, subject, message)


#
# @app.route("/blog")
# def blog():
#     return "<p>This is my first blog !</p>"

if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/static/about.html")
# def about():
#     return render_template("about.html")
#
# @app.route("/static/works.html")
# def work():
#     return render_template("works.html")
#
# @app.route("/static/contact.html")
# def contact():
#     return render_template("contact.html")
#
# @app.route("/static/index.html")
# def index():
#     return render_template("work.html")
#
# @app.route("/static/components.html")
# def components():
#     return render_template("components.html")
