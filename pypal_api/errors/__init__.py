class InvalidInputError(Exception):
    """
    This will be raised when one tries to input a type thats not in its
    list of types that can be used.
    """
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message