# se2-2026-lab01-Implementing-event-display-functionality-using-Flask-and-Git
Implementing event display functionality using Flask and Git
# Campus Events - Event Listing (Flask)
 
## Description
 
Campus Events is a web application developed using the Flask framework. In this lab assignment, the **Event Listing** functionality was implemented, allowing a list of events to be displayed on the application's main page.
 
The data is temporarily stored in memory (mock data) and rendered using HTML templates.
 
---
 
## Implemented Features
 
- Displaying a list of events.
- Flask main route (`/`).
- Separation of application logic from the HTML interface.
- Git integration for version control.
 
---
 
## Technologies Used
 
- Python 3.x
- Flask 3.0.2
- HTML5
- Git
- GitHub
 
---
 
## Project Structure
 
```text
campus-events/
│
├── app.py
├── requirements.txt
├── README.md
└── templates/
└── index.html
```
 
---
 
## Requirements
 
Before running the application, ensure that the following are installed:
 
- Python 3.x
- pip
- Git
 
Check the installed versions:
 
```bash
python --version
pip --version
git --version
```
 
---
 
## Installation
 
### 1. Clone the Repository
 
```bash
git clone https://github.com/uoradea-cti/se2-2026-lab01-Implementing-event-display-functionality-using-Flask-and-Git.git
```
 
Navigate to the project directory:
 
```bash
cd campus-events
```
 
### 2. Create a Virtual Environment
 
**Windows**
 
```bash
python -m venv venv
venv\Scripts\activate
```
 
**Linux / macOS**
 
```bash
python3 -m venv venv
source venv/bin/activate
```
 
### 3. Install Dependencies
 
```bash
pip install -r requirements.txt
```
 
---
 
## Configuration
 
The `requirements.txt` file contains:
 
```text
Flask==3.0.2
```
 
---
 
## Running the Application
 
Execute:
 
```bash
python app.py
```
 
The following message should appear in the terminal:
 
```text
* Running on http://127.0.0.1:5000
```
 
---
 
## Accessing the Application
 
Open your browser and navigate to:
 
```text
http://127.0.0.1:5000
```
 
Expected output:
 
```text
Campus Events
Upcoming Events
 
AI Workshop - 15.04.2025
Hackathon - 20.04.2025
Career Fair - 25.04.2025
```
 
---
 
## Main Application Code
 
### app.py
 
```python
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
```
 
---
 
## HTML Template
 
### templates/index.html
 
```html
<!DOCTYPE html>
<html>
<head>
<title>Campus Events</title>
</head>
<body>
 
<h1>Campus Events</h1>
 
<h2>Upcoming Events</h2>
 
<ul>
{% for event in events %}
<li>{{ event.title }} - {{ event.date }}</li>
{% endfor %}
</ul>
 
</body>
</html>
```
 
---
 
## Using Git
 
 
Add project files:
 
```bash
git add .
```
 
Create the commit:
 
```bash
git commit -m "Implement event listing functionality in Flask"
```
 
 
Push the project to GitHub:
 
```bash
git push -u origin main
```
 
---
 
## Assignment Objective
 
Implement the **Event Listing** functionality using Flask. The application must display a list of events on the homepage and follow the project structure and Git workflow described above.
 
---
 
## Deliverables
 
Students must submit:
 
- At least one commit containing the implemented functionality.
- A complete README file describing installation, execution, and project structure.
 
---

