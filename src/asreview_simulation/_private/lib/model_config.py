class ModelConfig:
    def __init__(self, abbr: str, params: dict):
        self.abbr = abbr
        self.params = params

    def asdict(self):
        return {
            "abbr": self.abbr,
            "params": self.params,
        }
