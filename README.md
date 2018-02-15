# cmdbus

## Using the command bus
```
from cmdbus import Bus, Command

class PrinterService:
    def print_text(text):
        print(text)

class PrintToConsoleCommand(Command):
    def __init__(self, printer_service, text):
        self.printer_service = printer_service
        self.text = text

    def handle():
        self.printer_service.print_text(text)

printer_service = PrinterService()
Bus.dispatch(PrintToConsoleCommand(printer_service, 'some text to print')
```