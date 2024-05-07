import pandas as pd

class HistoryManager:
    def __init__(self, filename='history.csv'):
        self.filename = filename
        self.load_history()

    def load_history(self):
        try:
            self.history = pd.read_csv(self.filename)
        except FileNotFoundError:
            self.history = pd.DataFrame(columns=['Operation', 'Result'])

    def add_record(self, operation, result):
        new_record = {'Operation': operation, 'Result': result}
        self.history = self.history.append(new_record, ignore_index=True)
        self.history.to_csv(self.filename, index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Operation', 'Result'])
        self.history.to_csv(self.filename, index=False)
