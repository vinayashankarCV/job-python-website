from flask import Flask,render_template
app=Flask(__name__)



JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengluru,India',
    'Salary':'Rs.10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi,India',
    'Salary':'Rs.30,00,000'
  },
  {
    'id':3,
    'title':'Data Scientist',
    'location':'Bengluru,India',
    'Salary':'Rs.15,00,000'
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS,)



if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
  