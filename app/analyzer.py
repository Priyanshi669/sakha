def analyze_behavior(activities):
    learning_time = 0
    execution_time = 0

    for act in activities:
        if act.type == "learning":
            learning_time += act.duration
        elif act.type in ["coding", "building"]:
            execution_time += act.duration

    total_time = learning_time + execution_time

    execution_ratio = (
        execution_time / total_time if total_time > 0 else 0
    )

    insights = []

    # Rules (your real intelligence)
    if learning_time > 3 * execution_time:
        insights.append("Overlearning detected")

    if execution_ratio < 0.3:
        insights.append("Low execution ratio")

    if total_time == 0:
        insights.append("No productive activity logged")

    suggestion = "Pick one task and complete it today"

    return {
        "learning_time": learning_time,
        "execution_time": execution_time,
        "execution_ratio": round(execution_ratio, 2),
        "insights": insights,
        "suggestion": suggestion,
    }
