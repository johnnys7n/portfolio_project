from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# def contacts_to_file(data):
#     with open('database.txt', 'a') as file:
#         for key, value in data.items():
#             file.write(f'\n {key} : {value}')

# populates .csv database with information from contacts
def contacts_to_csv(data):
    with open('database.csv', 'a', newline ='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']

        csv_writer = csv.writer(database, delimiter =',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            contacts_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else: 
        return 'something went wrong. Try again'


