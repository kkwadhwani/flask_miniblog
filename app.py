from flask import Flask, render_template, request
import datetime as dt
import database

app= Flask(__name__)
database.create_tables()

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=="POST":
        entry_content= request.form.get("content")
        database.insert_entry(entry_content, dt.datetime.today().strftime("%b %d") )


    return render_template("home.html", entries=database.retrieve_entries())


if __name__=="__main__":
    app.run(debug=True)