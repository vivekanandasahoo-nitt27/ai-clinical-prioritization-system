def calculate_severity(age, symptom_level, duration, model_confidence, existing_conditions=None):
    """
    Returns:
        severity_score (0-10 scale)
        emergency_flag (True/False)
    """

    severity = 0

    # -------------------------
    # 1️⃣ Model Confidence Impact (Small Weight)
    # -------------------------
    try:
        confidence = float(model_confidence)
        severity += confidence * 2  # Max contribution ~2
    except:
        pass

    # -------------------------
    # 2️⃣ Age Risk
    # -------------------------
    if age >= 75:
        severity += 2
    elif age >= 60:
        severity += 1

    # -------------------------
    # 3️⃣ Symptom Level
    # -------------------------
    if symptom_level == "Severe":
        severity += 2
    elif symptom_level == "Moderate":
        severity += 1

    # -------------------------
    # 4️⃣ Duration
    # -------------------------
    if duration == ">3 days":
        severity += 1

    # -------------------------
    # 5️⃣ Existing Conditions
    # -------------------------
    if existing_conditions:
        severity += min(len(existing_conditions), 2)

    # Normalize to max 10
    severity = min(severity, 10)

    emergency_flag = severity >= 8.5

    return round(severity, 2), emergency_flag