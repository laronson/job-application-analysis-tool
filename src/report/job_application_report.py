from typing import TypedDict
from datetime import date


class JobApplicationReportDetails(TypedDict):
    title: str
    company: str
    link: str
    date_posted: date
    analysis: str


class JobApplicationReport:
    def __init__(self, report_details: JobApplicationReportDetails):
        self.report_details = report_details

    def generate_report(self):
        datePosted = self.report_details.get("date_posted").strftime("%d/%m/%Y")
        return f"""Company: {self.report_details.get("company")}\nTitle: {self.report_details.get("title")}\nLink To Application: {self.report_details.get("link")}\nDate Posted: {datePosted}\n-----------------------------------------------------------------------\nAnalysis:\n{self.report_details.get("analysis")}"""
