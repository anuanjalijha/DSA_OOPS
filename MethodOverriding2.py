class Square:
    def drawSquare(self,length):
        print('drawing square of side: ', length)
        
class filledSquare(Square):
    def drawSquare(self,length):
        super().drawSquare(length)
        print('filling the square...')
        
square = filledSquare()
square.drawSquare(20)