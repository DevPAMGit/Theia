from abc import ABC

import colorama
from termcolor import colored

from TheiaInterface import TheiaInterface
from models.MessageType import MessageType


class Theia(TheiaInterface, ABC):
    """
    Principal class for Theia.
    """

    def __init__(self):
        """
        Initialize a new instance of Theia class.
        """
        # Initializing the console color.
        colorama.init()
        self.__INPUT__: str = "> "

    def listen(self) -> str:
        """
        Listen to Theia for client input.
        :return: The client input.
        """
        self.classic(self.__INPUT__)
        return input()

    def error(self, message: str = "", line_to_erase: bool = False):
        """
        Write an error message on the standard output.
        :param message: The message to write.
        :param line_to_erase: Indicate if the line need to be removed.
        """
        self.__write__(MessageType.ERROR, message, line_to_erase)

    def warning(self, message: str = "", line_to_erase: bool = False):
        """
        Write a warning message on the standard output.
        :param message: The message to write.
        :param line_to_erase: Indicate if the line need to be removed.
        """
        self.__write__(MessageType.WARNING, message, line_to_erase)

    def information(self, message: str = "", line_to_erase: bool = False):
        """
        Write an information message on the standard output.
        :param message: The message to write.
        :param line_to_erase: Indicate if the line need to be removed.
        """
        self.__write__(MessageType.INFORMATION, message, line_to_erase)

    def success(self, message: str = "", line_to_erase: bool = False):
        """
        Write a success message on the standard output.
        :param message: The message to write.
        :param line_to_erase: Indicate if the line need to be removed.
        """
        self.__write__(MessageType.SUCCESS, message, line_to_erase)

    def classic(self, message: str = "", line_to_erase: bool = False):
        """
        Write a classic message on the standard output.
        :param message: The message to write.
        :param line_to_erase: Indicate if the line need to be removed.
        """
        self.__write__(MessageType.CLASSIC, message, line_to_erase)

    @staticmethod
    def __write__(message_type: MessageType, message: str, erase_previous_line: bool = False):
        end: str = "\r" if erase_previous_line is True else ""

        # If there is no message, there io no print.
        if message.strip().__eq__(""):
            return

        if message_type.value.__eq__("ERROR"):
            print(colored(message, "light_red"), end=end)

        elif message_type.value.__eq__("WARNING"):
            print(colored(message, "light_yellow"), end=end)

        elif message_type.value.__eq__("SUCCESS"):
            print(colored(message, "light_green"), end=end)

        elif message_type.value.__eq__("INFORMATION"):
            print(colored(message, "light_cyan"), end=end)

        elif message_type.value.__eq__("CLASSIC"):
            print(colored(message, "white"), end=end)
