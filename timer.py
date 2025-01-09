import time


class Timer:
    def __init__(self, duration):
        self.initial_time = 0
        self.duration = duration
    
    def calculate_diff(self):
        return time.time() - self.initial_time

    def start(self):
        self.initial_time = time.time()

        return self
    
    def is_finished(self):
        return self.calculate_diff() >= self.duration
