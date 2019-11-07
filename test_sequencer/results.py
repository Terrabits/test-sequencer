import csv

class Results:
    def __init__(self, results_dicts):
        self.results_dicts = results_dicts

    def write_csv(self, filename):
        with open(filename, 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(list(self.results_dicts[0].keys()))
            for result in self.results_dicts:
                csv_writer.writerow(list(result.values()))
