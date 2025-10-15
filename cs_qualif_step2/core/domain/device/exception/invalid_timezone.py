from cs_qualif_step2.core.domain.exception.Invalid_input_exception import InvalidInputException


class InvalidTimezone(InvalidInputException):
    def __init__(self, timezone: str):
        self.firmware = timezone
        super().__init__(f"Invalid timezone: {timezone}, Aller pôv' type")