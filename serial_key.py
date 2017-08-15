"""Serial-Key, Keyboard emulator reading on a serial port

Usage:
    python {__file__} [-h|--help] [port [baud rate]]

The program will automatically try to detect a port where a micro:bit is
connected. If unsuccessful, it is possible to explicitly specify a port on the
command line. For example

    python {__file__} {serial_ports_list[0]}

The following are the available serial ports on this computer:

{serial_ports_string}

The following are key presses understood by the keyboard emulator:

{keys_string}
"""

# Standard library imports
import sys
import textwrap

# External library imports
from serial.tools import list_ports
import serial
import pyautogui

# Baud rate used if no rate is specified on the command line
DEFAULT_BAUDRATE = 115200


def list_serial_ports():
    """List all available serial ports

    Returns:
        List:  Names of all available serial ports.
    """
    return sorted(p[0] for p in list_ports.comports())


def detect_microbit_port():
    """Automatically detect which serial port is connected to micro:bit

    Returns None if no micro:bit is detected.

    Returns:
        String: Name of port where micro:bit is connected or None.
    """
    ports = list_ports.comports()
    for dev, _, spec in ports:
        if 'VID:PID=0d28:0204' in spec:
                return dev


def emulate(port, baudrate):
    """Send data from serial port to keyboard emulator

    Sends lines read from serial port (terminated with \n) as keypresses, until
    program is stopped by Ctrl-C (KeyboardInterrupt).

    Args:
        port (String):   Name of serial port.
        baudrate (int):  Baud rate.
    """
    print('Listening to serial port {} (baud rate {})'.format(port, baudrate))
    print('Press Ctrl-C to stop')

    try:
        with serial.Serial(port, baudrate) as ser:
            while True:
                key = ser.readline().decode().strip()
                print(key)
                pyautogui.press(key)
    except KeyboardInterrupt:
        pass


def help():
    """Print a help message

    Prints out the doc-string of the module, adding in some information about
    serial ports and available key presses.
    """
    serial_ports = list_serial_ports()
    keys_string = ', '.join(repr(k) for k in pyautogui.KEYBOARD_KEYS)
    help_text = __doc__.format(serial_ports_string='\n'.join(serial_ports),
                               serial_ports_list=serial_ports,
                               keys_string=textwrap.fill(keys_string, width=80),
                               **globals())
    print(help_text)


def main():
    """Read command line arguments and start emulation.

    If a serial port is not given, the program tries to detect which port a
    micro:bit is connected at. If unsuccessful, a help message is printed.
    """

    # Read or detect serial port
    try:
        port = sys.argv[1]
    except IndexError:
        port = detect_microbit_port()
    if port is None or '-h' in sys.argv or '--help' in sys.argv:
        return help()

    # Read baud rate or use default
    try:
        baudrate = sys.argv[2]
    except IndexError:
        baudrate = DEFAULT_BAUDRATE

    emulate(port, baudrate)


if __name__ == '__main__':
    main()
