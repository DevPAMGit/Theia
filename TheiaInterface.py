from abc import ABC, abstractmethod


class TheiaInterface(ABC):
    """
    Interface for Theia.
    """

    @abstractmethod
    def listen(self) -> str:
        """
        Listen to Theia for client input.
        :return: The client input.
        """
        pass

    @abstractmethod
    def error(self, message: str = "", line_to_erase: bool = False):
        """
        Write an error message on the standard output.
        :param message: The message to write.
        :param line_to_erase: Indicate if the line need to be removed.
        """
        pass

    @abstractmethod
    def warning(self, message: str = "", line_to_erase: bool = False):
        """
        Write a warning message on the standard output.
        :param message: The message to write.
        :param line_to_erase: Indicate if the line need to be removed.
        """
        pass

    @abstractmethod
    def information(self, message: str = "", line_to_erase: bool = False):
        """
        Write an information message on the standard output.
        :param message: The message to write.
        :param line_to_erase: Indicate if the line need to be removed.
        """
        pass

    @abstractmethod
    def success(self, message: str = "", line_to_erase: bool = False):
        """
        Write a success message on the standard output.
        :param message: The message to write.
        :param line_to_erase: Indicate if the line need to be removed.
        """
        pass

    @abstractmethod
    def classic(self, message: str = "", line_to_erase: bool = False):
        """
        Write a classic message on the standard output.
        :param message: The message to write.
        :param line_to_erase: Indicate if the line need to be removed.
        """
        pass
