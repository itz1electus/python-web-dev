from flask import Flask, render_template, jsonify

app = Flask(__name__)

COMPANY_NAME = "Jovian"
JOBS = [
    {
        'id': 1,
        'position': 'Data Analyst',
        'location': 'Indore, India',
        'salary': '₹10,00,000',
    },
    {
        'id': 2,
        'position': 'Data Scientist',
        'location': 'Mumbai, India',
        'salary': '₹15,00,000',
    },
    {
        'id': 3,
        'position': 'Web Designer',
        'location': 'Lagos, Nigeria',
        'salary': '₦1,000,000',
    },
    {
        'id': 4,
        'position': 'Front End Designer',
        'location': 'New York City, USA',
        'salary': '$100,000',
    },
]


@app.route("/")
def template():
    return render_template("home.html", jobs=JOBS, company_name=COMPANY_NAME)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
