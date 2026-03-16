from gen_report import BaseReportHandler, CoffieMedianReportHandler

def choice_report_handler(param_repo: str) -> BaseReportHandler | None:
    handlers = {CoffieMedianReportHandler.slug: CoffieMedianReportHandler()}
    if param_repo not in handlers:
        return None
    return handlers[param_repo]