from enum import Enum


class MessageType(Enum):
    """
    Enumeration for available message types.
    """
    # Indicate an error message
    ERROR: str = "ERROR"
    # Indicate a warning message
    WARNING: str = "WARNING"
    # Indicate a success message
    SUCCESS: str = "SUCCESS"
    # Indicate a classic message
    CLASSIC: str = "CLASSIC"
    # Indicate an information message
    INFORMATION: str = "INFORMATION"

    # @staticmethod
    # def maximum_space() -> int:
    #     """
    #     Get the maximum size (in number of characters) of the largest enumeration.
    #     :return: The maximum size (in number of characters) of the largest enumeration.
    #     """
    #     value: int = 0
    #     for enum_value in MessageType:
    #         len_enum_value: int = len(enum_value.value)
    #         if len_enum_value.__gt__(value):
    #             value = len_enum_value
    #     return value
