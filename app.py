from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for the dashboard
project_info = {
    "project_name": "CI/CD Pipeline Demo",
    "status": "Running",
    "version": "v1.0.0",
    "description": "This is a demo project showcasing CI/CD automation using GitHub Actions and Docker.",
    "owner": "srrevis"
}

@app.route("/")
def project_dashboard():
    return render_template('dashboard.html', project=project_info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
