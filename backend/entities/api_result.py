class APIResult:
    def __init__(self, status: str, data: str):
        self.status = status
        self.data = data

    def dictify(self):
        return {
            "status": self.status,
            "data": self.data
        }
