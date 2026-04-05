
from log_ai import LogAI


log_path = input("Log dosyası: ")

app = LogAI(log_path)
app.run()   