from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')  # index.html root page
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')  # redirecting the pages dynamically
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):  # writing to the database/text(database.txt) file so that information can be viewed later
    with open('database.txt', mode='a') as database:
        name  = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {name},{email},{subject},{message}')


def write_to_csv(data):  # writing to the database/text(database.csv) file so that information can be viewed later
    with open('database.csv', newline='', mode='a') as database2:
        name  = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar=';',
                                quoting=csv.QUOTE_MINIMAL)  # for more info check csv python documentation
        csv_writer.writerow([name,email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])  # submitting the form by the user and redirecting the user to
# thankyou.html page

def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)

        except:
            return 'did not save to the database'
    else:
        return 'something went wrong.Try again'
    name = request.form['name']
    return render_template('thankyou.html', name=name)
