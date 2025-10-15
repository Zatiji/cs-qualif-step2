from cs_qualif_step2.core.domain.exception.Invalid_input_exception import InvalidInputException


class InvalidFirmwareVersion(InvalidInputException):
    def __init__(self, firmware: str):
        self.firmware = firmware
        super().__init__(f"Invalid firmware version : {firmware}, Aller pôv' type")