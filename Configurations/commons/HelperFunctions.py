from enum import Enum

class HelperFuncs(Enum):

    @staticmethod
    def openFiles(filePath):
        return open(filePath, 'r')

    @staticmethod
    def STATUS200():
        return 200

    @staticmethod
    def STATUS201():
        return 201

    @staticmethod
    def STATUS400():
        return 400

    @staticmethod
    def STATUS404():
        return 404

    @staticmethod
    def STATUS500():
        return 500

    @staticmethod
    def STATUS503():
        return 503
