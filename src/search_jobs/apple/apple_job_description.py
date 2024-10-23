from ..models import JobDescription


class AppleJobDescription(JobDescription):
    def __init__(self, jd):
        super().__init__(job_description_attributes=jd)
        self.raw = jd

    def get_raw(self):
        return self.raw
