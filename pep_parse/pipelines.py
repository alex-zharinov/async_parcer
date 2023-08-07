import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


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
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.data.items():
                f.write(f'{status},{count}\n')
            f.write(f'Total,{self.total}\n')
