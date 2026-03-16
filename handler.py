from gen_report import BaseReportHandler, CoffieMedianReportHandler

def choice_report_handler(param_repo: str) -> BaseReportHandler:
    handlers = {CoffieMedianReportHandler.slug: CoffieMedianReportHandler()}
    return handlers[param_repo]