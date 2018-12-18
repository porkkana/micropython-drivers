class PCF8575(object):
    def __init__(self):
        self._PIN = 0
        self._DDR = 0
        self._PORT = 0
    
    def toggle(self, pin):
        self._PORT ^= (1 << pin)
        self.updateGPIO()
    
    def updateGPIO(self):
        value = (self._PIN & ~self._DDR) | self._PORT
        
        print('{0:08b}'.format(value & 0x00FF))
        print('{0:08b}'.format((value & 0xFF00) >> 8))
    
    def digitalWrite(self, pin, value):
        if value:
            self._PORT |= (1 << pin)
        else:
            self._PORT &= ~(1 << pin)
        self.updateGPIO()
    
    def readGPIO(self):
        pass

# a = PCF8575()
#
# a.digitalWrite(1, 1)
# a.toggle(1)
# a.toggle(1)
