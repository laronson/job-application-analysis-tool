from ..base import JobDescription


class AppleJobDescription(JobDescription):
    def __init__(self, jd):
        super().__init__(company="apple", config=jd)
        self.raw = jd

    def get_raw(self):
        return self.raw
