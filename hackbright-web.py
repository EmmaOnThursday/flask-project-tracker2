from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)



@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)
    return html


@app.route("/add-student", methods=['POST'])
def add_new_student_form():
    """Show form for adding a new student. """

    return render_template("student_add_form.html")



@app.route("/new-student")
def display_new_student():
    """After student is added, display student info."""


    first = request.form.get('first_name', 'Jane')
    last = request.form.get('last_name', 'Hacks')
    github = request.form.get('github', 'jhacks')

    first, last, github = hackbright.get_student_by_github(first_name, last_name, github)

    return render_template("new_student.html",                             
                            first=first,
                            last=last,
                            github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
