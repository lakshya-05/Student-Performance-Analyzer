import pandas as pd
import io
from analysis import *
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/FullAnalysis')
def fda():
    return render_template('full.html',total_avg=total_avg,total_stu=total_stu, toppers=toppers)

@app.route('/IndividualAnalysis', methods=["GET", "POST"])
def ida():
    result = None
    if request.method == "POST":
        full_name = request.form.get("stuname", "").strip().lower()
        
        if full_name:
            match = data[data["full_name"] == full_name]

            if not match.empty:
                student = match.iloc[0]
                result = {
                    "name": f"{student['first_name']} {student['last_name']}",
                    "marks": student["score"],
                    "hours": student["weekly_self_study_hours"],
                    "subject_scores": {
                        "Math": student["math_score"],
                        "History": student["history_score"],
                        "Physics": student["physics_score"],
                        "Chemistry": student["chemistry_score"],
                        "Biology": student["biology_score"],
                        "English":student["english_score"],
                        "Geography":student["geography_score"]
                    }
                }
            else:
                result = "Student not found"
    return render_template('individual.html', result=result)

@app.route('/plot/<student_name>')
def plot(student_name):
    full_name = student_name.strip().lower()
    match = data[data["full_name"] == full_name]

    if match.empty:
        return "Student not found", 404

    student = match.iloc[0]

    subject_scores = {
        "Math": student["math_score"],
        "History": student["history_score"],
        "Physics": student["physics_score"],
        "Chemistry": student["chemistry_score"],
        "Biology": student["biology_score"],
        "English": student["english_score"],
        "Geography": student["geography_score"]
    }

    avg_scores = {
        "Math": math_avg,
        "History": history_avg,
        "Physics": physics_avg,
        "Chemistry": chemistry_avg,
        "Biology": biology_avg,
        "English": english_avg,
        "Geography": geography_avg
    }

    subjects = list(subject_scores.keys())
    student_marks = list(subject_scores.values())
    class_avgs = [avg_scores[subj] for subj in subjects]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(subjects, student_marks, color='royalblue', label='Student')
    plt.plot(subjects, class_avgs, color='crimson', linestyle='--', marker='o', label='Class Average')
    plt.axhline(y=total_avg, color='orange', linestyle='-.', linewidth=2, label=f"Overall Avg ({total_avg})")

    plt.ylim(0, max(student_marks + class_avgs) + 20)

    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(i, height + 3, f"{height:.1f}", ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')


    plt.ylim(0, 105)
    plt.ylabel("Score out of 100")
    plt.title(f"{student['first_name']} {student['last_name']} - Subject Performance")
    plt.legend()
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
