from ..base import RequesterConfig


class AppleRequesterConfig(RequesterConfig):
    csrf_path: str


apple_config: AppleRequesterConfig = {
    "base_url": "https://jobs.apple.com/api/",  # must add / at the end to get urljoin to work
    "search_path": "role/search",
    "details_path": "role/detail",
    "csrf_path": "csrfToken",
}

location_transform = {
    "washington": "postLocation-state1000",
    "seattle": "postLocation-SEA",
    "boston": "postLocation-BST",
}
