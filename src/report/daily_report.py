from datetime import datetime
from .job_application_report import JobApplicationReport, JobApplicationReportDetails
from typing import List


class DailyReport:
    def __init__(self, report_directory_path):
        self.jobs: List[JobApplicationReport] = []
        self.report_directory_path = report_directory_path

    def add_job(self, application_report_details: JobApplicationReportDetails):
        self.jobs.append(JobApplicationReport(application_report_details))

    def generate_report(self):
        filename = f"{datetime.now().strftime("%m-%d")}.md"
        with open(f"{self.report_directory_path}{filename}", "w+") as file:
            for job in self.jobs:
                file.write(f"{job.generate_report()}\n")
