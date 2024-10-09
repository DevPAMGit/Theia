from abc import ABC
from typing import Optional

import colorama
from termcolor import colored

from TheiaInterface import TheiaInterface
from TheiaListener import TheiaListener
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
        # Set the input start.
        self.__INPUT__: str = "> "
        # Initialize the view's listener.
        self.__listener__: Optional[TheiaListener] = None

    def suscribe(self, listener: TheiaListener):
        """
        Set the view's listener.
        :param listener: The new view's listener.
        """
        self.__listener__ = listener

    def light(self):
        """
        Run Theia.
        """
        # Get the client first command.
        client_input: str = self.__get_input__()

        # While 'exit 'keyword
        while client_input.__ne__("exit"):

            if client_input.__ne__(""):
                # If there is listener: notify him.
                if self.__listener__ is not None:
                    self.__listener__.notify(client_input)

            client_input = self.__get_input__()

        # 'exit' keyhword found': unsucribe the listener.
        # If there is listener: unsuscribe him.
        if self.__listener__ is not None:
            self.__listener__.unsuscribe()

        # Reset the listener.
        self.__listener__ = None

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

    def __get_input__(self) -> str:
        """
        Get the client input.
        :return: The client input.
        """
        self.__write__(MessageType.CLASSIC, self.__INPUT__)
        return input().strip()

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
