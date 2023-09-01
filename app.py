from flask import Flask , render_template, jsonify
app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title': 'Data Analyst',
    'location' : 'Ljubljana, Slovenija',
    'salary' : 'EUR 1700'
  },
  {
    'id':2,
    'title': 'UI designer',
    'location' : 'Koper, Slovenija',
    'salary' : 'EUR 1450'
  },
  {
    'id':3,
    'title': 'Fullstack Dev',
    'location' : 'Remote',
    'salary' : 'EUR 2500'
  },
  {
    'id':4,
    'title': 'Mobile dev',
    'location' : 'Vienna, Austria',
    'salary' : 'EUR 3000'
    
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs = JOBS)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True) 