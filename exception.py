class CustomException(Exception):
    pass

class EnclosureFullException(CustomException):
    pass

class AnimalFullException(CustomException):
    pass

class SingleSpeciesException(CustomException):
    pass

class IDEnclosureException(CustomException):
    pass

class EnclosureCleanedException(CustomException):
    pass

class UnsufficientHealthRecordException(CustomException):
    pass

class InsufficientSeverityException(CustomException):
    pass

class AnimalTreatmentException(CustomException):
    pass