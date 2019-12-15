from   .helpers import is_dict, prefix_keys
import csv

class Results:
    def __init__(self, results_dicts=[]):
        self.results_dicts = results_dicts

    @property
    def headers(self):
        if not self.results_dicts:
            return []
        headers = []
        for key in self.results_dicts[0]:
            value = self.results_dicts[0][key]
            if is_dict(value):
                prefixed_value = prefix_keys(value, key)
                headers += list(prefixed_value.keys())
            else:
                headers.append(key)
        return headers

    @property
    def rows(self):
        return [self.row(i) for i in range(0, len(self.results_dicts))]

    def row(self, i):
        row = []
        results = self.results_dicts[i]
        for key in results:
            value = results[key]
            if is_dict(value):
                values = list(results[key].values())
                row += values
            else:
                row.append(value)
        return row

    def write_csv(self, filename):
        with open(filename, 'w') as f:
            if not self.results_dicts:
                # touch file and return
                return
            csv_writer = csv.writer(f)
            csv_writer.writerow(self.headers)
            for row in self.rows:
                csv_writer.writerow(row)
