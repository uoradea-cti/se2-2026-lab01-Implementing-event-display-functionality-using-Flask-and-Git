from flask import Flask, render_template
 
app = Flask(__name__)
 
events = [
{"title": "AI Workshop", "date": "15.04.2025"},
{"title": "Hackathon", "date": "20.04.2025"},
{"title": "Career Fair", "date": "25.04.2025"}
]
 
@app.route("/")
def index():
  return render_template("index.html", events=events)
 
if __name__ == "__main__":
  app.run(debug=True)
