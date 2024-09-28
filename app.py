from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for the dashboard
project_info = {
    "project_name": "CI/CD Pipeline Demo",
    "status": "Running",  # Change to "Stopped" to test different status states
    "version": "v1.0.0",
    "description": "This is a demo project showcasing CI/CD automation using GitHub Actions and Docker.",
    "owner": "srrevis",
    "deployments": 15,
    "tests_passed": 120,
    "issues_resolved": 45,
    "progress_percentage": 70  # This is for the progress bar
}

@app.route("/")
def project_dashboard():
    return render_template('dashboard.html', project=project_info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
