from gen_report import BaseReportHandler, CoffieMedianReportHandler


def choice_report_handler(param_repo: str) -> BaseReportHandler | None:
    handlers = {CoffieMedianReportHandler.slug: CoffieMedianReportHandler}
    return handlers.get(param_repo)
