from typing import List
from collections import defaultdict
from statistics import median

class BaseReportHandler:
    def process(self, data: List[dict]) -> List[tuple]:
        pass


class CoffieMedianReportHandler(BaseReportHandler):
    slug = 'median-coffee'
    
    def process(self, data: List[dict]) -> List[tuple]:
        report_dict = defaultdict(list)
        result_list = []
        for item in data:
            report_dict[item['student']].append(float(item['coffee_spent']))
        for item in report_dict:
            result_list.append(tuple((item, median(report_dict[item]))))
            result_list.sort(key=lambda x: (-x[1], x[0]))
        return result_list