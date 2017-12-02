from qrtools import QR
import webbrowser
import time
myCode = QR()
myCode.decode_webcam(lambda data: webbrowser.open(data),device='/dev/video0')


    





