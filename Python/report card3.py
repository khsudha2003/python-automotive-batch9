def check_pass_fail(score):
    """Checks if a score is a pass (>= 60) or fail."""
    if score >= 60:
        return "PASS"
    else:
        return "FAIL"

# --- Example Usage ---

student_name = "Alice"
math_score = 75
history_score = 55

print(f"--- {student_name}'s Report Card ---")
print(f"Math: {math_score} - Status: {check_pass_fail(math_score)}")
print(f"History: {history_score} - Status: {check_pass_fail(history_score)}")