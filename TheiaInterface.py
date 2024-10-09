from abc import ABC, abstractmethod

import TheiaListener


class TheiaInterface(ABC):
    """
    Interface for Theia.
    """

    @abstractmethod
    def light(self):
        """
        Run Theia.
        """
        pass

    @abstractmethod
    def suscribe(self, listener: TheiaListener):
        """
        Set the view's listener.
        :param listener: The new view's listener.
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
