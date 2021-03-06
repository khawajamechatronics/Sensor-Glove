import serial


#port1 = serial.Serial(port='COM4', baudrate=115200, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, timeout=None)
port1 = serial.Serial(port='COM3', baudrate=9600, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, timeout=None)
#port1 = serial.Serial(port='COM7', baudrate=9600, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, timeout=None)


def __init__(self):
    self.data = []


def flush_input():
    port1.flushInput()


def InputBuffer_Length():
    byte_length = port1.inWaiting()
    return byte_length


def read_8():
    return port1.read()


def read_line():
    return port1.readline()


def read_text():
    startbit = b's'
    endbit = b'\n'
    message = []
    while True:
        buffer = port1.read()
        if(buffer == startbit):
            while(buffer != endbit):
                buffer = port1.read()
                message.append(chr(buffer[0]))
            break
        else:
            port1.flushInput()
    message = message[:-1]
    string_buffer = ''.join((message))
    return string_buffer

def text_to_decimal():
    return float(read_text())


def wait():
    port1.inWaiting()


def write_8(data):
    message = data.encode('utf-8')
    port1.write(message)

def write_dec(data):
    if(data > 256):
        m1 = str.encode(chr(data))
        port1.write(m1)
    else:
        m1 = str.encode(chr(0))
        m2 = str.encode(chr(data))
        port1.write(m1)
        port1.write(m2)


def read_num():
    temp_a = port1.read()
    number = ord(temp_a)
    return number


def read_dec():
    temp_a = port1.read()
    temp_b = port1.read()
    temp_c = (temp_b[0] << 8) | temp_a[0]
    return temp_c


def read_32():
    temp_a = port1.read()
    temp_b = port1.read()
    temp_c = port1.read()
    temp_d = port1.read()
    value = (temp_d[0] << 24) | (temp_c[0] << 16) | (temp_b[0] << 8) | temp_a[0]
    print(value)


def print_Sensor():
    temp_a = port1.read()
    temp_b = port1.read()
    sensor = (temp_b[0] << 8) | temp_a[0]
    print('Sensor Value: {:f}'.format(sensor))


def read_hex():
    temp_a = port1.read()
    temp_b = port1.read()
    temp_c = (temp_b[0] << 8) | temp_a[0]
    temp_a = hex(temp_c)
    return temp_a


def print_32(self):
    temp_a = port1.read_8()
    temp_b = port1.read_8()
    temp_c = port1.read_8()
    temp_d = port1.read_8()
    temp_e = (temp_b[0] << 8) | temp_a[0]
    temp_f = (temp_c[0] << 8) | temp_d[0]
    print(temp_e)
    print(temp_f)


def print_ID(self, event):
    deviceID = self.read_hex()
    print('Device ID: ' + repr(deviceID))


def print_ID(self):
    deviceID = self.read_hex()
    print('Device ID: ' + repr(deviceID))


def print_Voltage(self):
    analog = self.read_dec()
    voltage = (analog/1024 * 5)
    print('Voltage: {:f}'.format(voltage))


def print_Name(self):
    print("Huggie!")


def update_Sensor(self, g, t):
    print(str(t))
