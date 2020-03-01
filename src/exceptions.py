
class OverStep(Exception):
    def __init__(self, message="Step quantity over maximum safety", errors):
            super().__init__(message)
