class Road:
    # Set length and width equal to zero to start
    # Feet in a mile = 5280
    # Inch in ft = 1/12
    def __init__(self):
        self.__length = 0
        self.__width = 0

    # This function inputs width in feet
    def setWidth(self, width):
        self.__width = width

    # This function inputs length in miles
    def setLength(self, length):
        self.__length = length

    # This function returns width
    def getWidth(self):
        return self.__width

    # This function returns length
    def getLength(self):
        return self.__length

    # This function returns the asphalt needed to make the road in cubic feet
    def asphaltNeeded(self, thickness):
        mileFt = 5280
        oneInch = 1/12
        length = mileFt * self.__length
        thicknessFt = thickness * oneInch

        return length * self.__width * thicknessFt

def driver():
    test_road = Road()
    test_road.setLength()
    test_road.setWidth()
    print(test_road.getWidth())
    print(test_road.getLength())
    print(test_road.asphaltNeeded())


if __name__ == '__main__':
    driver()
