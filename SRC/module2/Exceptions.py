class InvalidSalaryError(Exception):
    pass
def calculate(salary):
    if salary<=0:
        raise InvalidSalaryError("slary must be greatr than zero")
    print("valid")