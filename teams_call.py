import os
import sys
from pathlib import Path

def getLogFile():
    if sys.argv[1]:
        return sys.argv[1]

    if os.uname().sysname == 'Linux':
        return str(Path.home()) + '/.config/Microsoft/Microsoft Teams/logs.txt'
    if os.uname().sysname == 'Darwin':
        return str(Path.home()) + '/Library/Application Support/Microsoft/Teams/logs.txt'

    raise Exception('logs file path not given as argument or OS not supported!')

def isInCall():
    logFile = getLogFile()
    if not os.path.isfile(logFile):
        print(f'Log file not found: {logFile}')
        return False

    output = os.popen('tac "' + logFile +  '" | grep -oh "eventData: s::;m::1;a::[0-9]" | head -n1').read().split('\n')

    try:
        return output[0][-1] in ['0', '1']
    except Exception as err:
        print("Error:", err)
        return False

if __name__ == '__main__':
    isInCall()
