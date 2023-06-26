import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
     QPlainTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import QProcess

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a button and connect it to the start_process method
        self.btn = QPushButton("Get IPv4 Addresses")
        self.btn.pressed.connect(self.start_process)
        # Create a text area to display the output
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)
        # Create a layout and add the button and text area to it
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.text)
        # Create a central widget, set the layout and set it as central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setFixedSize(400, 200)

    def start_process(self):
        # Create a QProcess object
        self.process = QProcess()
        # Connect the readyReadStandardOutput signal to the handle_output method
        self.process.readyReadStandardOutput.connect(self.handle_output)
        # Start the external command
        # Note: cmd /c is used to execute the command and then terminate the cmd process
        self.process.start("cmd", ["/c", "ipconfig /all | findstr IPv4"])

    def handle_output(self):
        # Read the standard output of the process
        data = self.process.readAllStandardOutput()

        # Decode the bytes to string and append it to the text area
        output = bytes(data).decode("utf-8")
        self.text.appendPlainText(output)

# Create the Qt Application
app = QApplication(sys.argv)
# Create and show the main window
window = MainWindow()
window.show()
# Run the main Qt loop
sys.exit(app.exec_())
