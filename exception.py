"""
File: exception.py
Description: This file is where all the exceptions are handled and all the exceptions for the other files are
called here.
Author: Jack Gallagher
ID: 110410979
Username: galjh002
This is my own work as defined by the University's Academic Integrity Policy.
"""

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