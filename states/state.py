from datetime import datetime


class TaskDeadlineState:
    def __init__(self, subject):
        self._subject = subject
        self._deadline = None

    def set_deadline(self, deadline):
        self._deadline = deadline
        self._subject.notify()

    def check_deadline(self):
        if self._deadline and datetime.now() >= self._deadline:
            self._subject.is_completed = True
            self._subject.color = "red"
            self._subject.notify()
