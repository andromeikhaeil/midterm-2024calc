class CommandHandler:
    def __init__(self):
        self.commands = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
        }

    def handle_command(self, input_str):
        parts = input_str.split()
        command = parts[0]
        args = map(float, parts[1:])
        if command in self.commands:
            return self.commands[command](*args)
        return "Unknown command"

    def add(self, *args):
        return sum(args)

    def subtract(self, *args):
        return args[0] - sum(args[1:])

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    def divide(self, *args):
        try:
            result = args[0]
            for num in args[1:]:
                if num == 0:
                    raise ValueError("Division by zero.")
                result /= num
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."