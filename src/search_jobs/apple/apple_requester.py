from ..base import Requester
from ..models import JobDescription
import requests
from typing import TypedDict, Dict, List, Any
from .config import apple_config, location_transform
from datetime import datetime


class AppleRequesterSearch(TypedDict):
    query: str
    page: int
    locale: str
    sort: str
    filters: Dict[str, Any]


class AppleRequester(Requester):
    def __init__(self):
        super().__init__(apple_config)
        self.company = "Apple"
        self.update_csrf_path = apple_config["csrf_path"]

    def find_new_job_openings(self, query) -> List[JobDescription]:
        new_job_opening_ids = self._find_jobs(query=query)

        jds = []
        for id in new_job_opening_ids:
            raw_description = self._find_job_description(id)
            if raw_description:
                job_description = self._map_to_job_description(job_id=id, company_jd=raw_description)
                jds.append(job_description)

        return jds

    def _map_to_job_description(self, job_id: str, company_jd: Dict[str, Any]) -> JobDescription:
        return JobDescription(
            job_description_attributes={
                "company": self.company,
                "company_id": job_id,
                "title": company_jd.get("postingTitle", ""),
                "team_summary": company_jd.get("jobSummary", ""),
                "job_description_summary": company_jd.get("description", ""),
                "locations": [location.get("name") for location in company_jd.get("locations", [])],
                "minimum_qualifications": company_jd.get("minimumQualifications", ""),
                "preferred_qualifications": company_jd.get("preferredQualifications", ""),
                "posting_date": (
                    datetime.fromisoformat(company_jd["postDateInGMT"]) if company_jd["postDateInGMT"] else None
                ),
            },
        )

    def _find_jobs(self, query) -> List[str]:
        self._update_csrf()

        url = self._format_url(self.search_path)
        params = self._format_search_parameters(parameters={"query": query, "locations": ["washington"]})

        self.session.headers.update({"Content-Length": f"{len(params) * 8}", "Content-Type": "application/json"})

        openings = self._post(parameters=params, url=url)

        ids = []
        if openings:
            for opening in openings["searchResults"]:
                ids.append(opening.get("id").split("-")[1])
        return ids

    def _find_job_description(self, job_id: str) -> Dict[str, Any] | None:
        self.session.cookies.clear()
        url = self._format_url(f"{self.details_path}/{job_id}")
        job_description = self._get(url=url)
        return job_description

    def _format_search_parameters(self, parameters: Dict[str, Any]) -> AppleRequesterSearch:
        query = parameters.get("query", "")
        locations = parameters.get("locations", [])

        posting_locations = []
        for location in locations:
            if location not in location_transform:
                raise Exception(f"Location {location} does not exist in location transforms")
            posting_locations.append(location_transform[location])

        return {
            "query": query,
            "locale": "en-us",
            "page": 1,
            "sort": "newest",
            "filters": {"postingpostLocation": posting_locations},
        }

    def _update_csrf(self):
        s = requests.Session()
        response = s.get(self._format_url(self.update_csrf_path))

        for header, value in response.headers.items():
            if header == "X-Apple-CSRF-Token":
                s.headers.update({"X-Apple-CSRF-Token": value})

        return s
