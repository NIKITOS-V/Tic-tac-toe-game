class ColorError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]

        else:
            self.message = "Uncorrected rgb value"

    def __str__(self):
        return self.message
