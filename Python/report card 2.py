student_scores = {
    "English": 82,
    "Science": 59,
    "Math": 91,
    "Art": 60
}

print("--- Student Report ---")
for subject, score in student_scores.items():
    status = "PASS" if score >= 60 else "FAIL"
    print(f"{subject}: {score} - Status: {status}")