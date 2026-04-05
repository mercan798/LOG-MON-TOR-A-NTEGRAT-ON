import time


class LogWatcher:

    def __init__(self, file):
        self.file = file

    def follow(self):
        self.file.seek(0, 2)

        while True:
            line = self.file.readline()

            if not line:
                time.sleep(0.2)
                continue

            yield line