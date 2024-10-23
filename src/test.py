from search_jobs.apple import AppleRequester
from models.openai import ChatGPT
from documents import Resume, CoverLetter
from dotenv import load_dotenv
from report import DailyReport
from datetime import datetime

load_dotenv()

ac = AppleRequester()
gpt = ChatGPT()
report = DailyReport(report_directory_path="./generated_reports/")
resume = Resume(file_name="leonard_aronson_resume.txt", file_path="./document_assets/resumes/", doc_type="text")
cover_letter = CoverLetter(file_name="cover_letter.txt", file_path="./document_assets/cover_letters/", doc_type="text")

jobs = ac.find_new_job_openings(query="200572383")

print("----------------- MODEL OUTPUT -----------------")
if jobs[0] and jobs[0]:
    job = jobs[0]
    attributes = jobs[0].get_base_attributes()
    analysis = gpt.call_model(
        company=job.company,
        job_description_text=job.get_text(),
        resume=resume.document_from_text(),
        cover_letter=cover_letter.document_from_text(),
    )
    report.add_job(
        {"title": job.title, "company": job.company, "link": "N/A", "analysis": analysis, "date_posted": datetime.now()}
    )

report.generate_report()
