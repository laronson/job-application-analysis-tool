from urllib.parse import urljoin
from typing import TypedDict, Dict, Any, List
import json
import requests


class RequesterConfig(TypedDict):
    base_url: str
    search_path: str
    details_path: str


class Requester:
    def __init__(self, config: RequesterConfig):
        self.base_url = config.get("base_url")
        self.search_path = config.get("search_path")
        self.details_path = config.get("details_path")
        self.session = requests.Session()

    def _post(self, url: str, parameters: object):
        response = self.session.post(url=url, data=json.dumps(parameters))

        if response.status_code == 200:
            return response.json()
        print(f"Request to {url} failed with code: {response.status_code} and message {response.reason}")

    def _get(self, url: str):
        self.session.headers.clear()
        response = self.session.get(url=url)

        if response.status_code == 200:
            return response.json()
        print(f"Request to {url} failed with code: {response.status_code} and message {response.reason}")

    def _format_url(self, path: str):
        return urljoin(base=self.base_url, url=path)

    def _find_jobs(self, query: str) -> List[str]:
        raise Exception("Function find_new_job_openings must be implemented in class extension")

    def _find_job_description(self, job_id: str) -> Dict[str, Any] | None:
        raise Exception("Function get_job_description must be implemented in class extension")

    def _format_search_parameters(self, parameters: Dict[str, Any]) -> Any:  # TODO: Use Generics
        raise Exception("Must implement search parameter function")
