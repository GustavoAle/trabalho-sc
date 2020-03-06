
class OverStep(Exception):
    def __init__(self, message="Step quantity over maximum safety", errors=None):
            super().__init__(message)
