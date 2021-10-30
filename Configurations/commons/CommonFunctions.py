from abc import abstractmethod, ABC


class CommonFunc(ABC):

    @abstractmethod
    def test_createGetRequest(self):
        pass

    @abstractmethod
    def test_createPostRequest(self):
        pass

    @abstractmethod
    def test_createPutRequest(self):
        pass

    @abstractmethod
    def test_createDeleteRequest(self):
        pass
