def handle_event(log_type, line):
    if log_type == "error":
        return "AI" 
    elif log_type == "warning":
        return "WARN"
    else:
        return "IGNORE"