from abc import ABC, abstractmethod


class TheiaListener(ABC):

    @abstractmethod
    def notify(self, message: str):
        """
        Notifyh the subscriber that Theia has message.
        :param message: Theia's message.
        """
        pass

    @abstractmethod
    def unsuscribe(self):
        """
        Unsubcribe the listenner to Theia.
        """
        pass
