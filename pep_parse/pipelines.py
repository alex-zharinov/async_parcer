import csv
import datetime as dt
from pathlib import Path

from .settings import DATETIME_FORMAT

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.data = {}
        self.total = 0

    def process_item(self, item, spider):
        if item['status'] not in self.data:
            self.data[item['status']] = 1
        else:
            self.data[item['status']] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_path = results_dir / file_name
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            )
            writer.writerows([
                ('Статус', 'Количество'),
                *self.data.items(),
                ('Total', self.total)
            ])
