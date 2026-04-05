from parser import parse_line
from ai import analyze_log
from livelog import LogWatcher
from event import handle_event

class LogAI:
    
    def __init__(self, log_path):
        self.log_path = log_path
        self.file = open(log_path, "r")
        
        
        
    def process_line(self, line):
        log_type = parse_line(line)
        action = handle_event(log_type, line)

        print(line, end="")

        if action == "AI":
            result = analyze_log(line)
            print("AI:", result)
            
    def run(self):
   
        watcher = LogWatcher(self.file)

        for line in watcher.follow():
            self.process_line(line) 