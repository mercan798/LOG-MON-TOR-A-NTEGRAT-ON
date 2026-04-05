def parse_line(line):
    if "ERROR" in line:
        return "error"
    elif "WARNING" in line:
        return "warning"
    else:
        return "info"