from cs_qualif_step2.core.domain.exception.Invalid_input_exception import InvalidInputException


class InvalidLocation(InvalidInputException):
    def __init__(self, location: str):
        self.firmware = location
        super().__init__(f"Invalid location : {location}, Aller pôv' type")