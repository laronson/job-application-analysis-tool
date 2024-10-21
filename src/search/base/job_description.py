from typing import TypedDict, List, Dict, Any
import json
from datetime import datetime, date


class JobDescriptionAttributes(TypedDict):
    company: str
    company_id: str
    title: str
    team_summary: str
    job_description_summary: str
    locations: List[str]
    minimum_qualifications: List[str]
    preferred_qualifications: List[str]
    posting_date: date | None


class JobDescription:
    def __init__(self, job_description_attributes: JobDescriptionAttributes):
        self.company = job_description_attributes.get("company", "")
        self.company_id = job_description_attributes.get("company_id")
        self.title = job_description_attributes.get("title")
        self.posting_date = job_description_attributes.get("posting_date")
        self.team_summary = job_description_attributes.get("team_summary")
        self.job_description_summary = job_description_attributes.get("job_description_summary")
        self.locations = job_description_attributes.get("locations")
        self.minimum_qualifications = job_description_attributes.get("minimum_qualifications")
        self.preferred_qualifications = job_description_attributes.get("preferred_qualifications")

    def get_base_attributes(self):
        return {
            "company": self.company,
            "company_id": self.company_id,
            "title": self.title,
            "posting_date": self.posting_date.strftime("%m-%d-%y") if self.posting_date else "Unknown",
            "locations": self.locations,
            "job_description_summary": self.job_description_summary,
            "team_summary": self.team_summary,
            "minimum_qualifications": self.minimum_qualifications,
            "preferred_qualifications": self.preferred_qualifications,
        }

    def get_text(self) -> str:
        return json.dumps(self.get_base_attributes())

    def get_raw(self) -> Dict[str, Any]:
        raise Exception("Must implement get_raw function in extended class")
