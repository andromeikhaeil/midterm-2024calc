from utils.logger import setup_logger
from commands import CommandHandler
from plugins import load_plugins

logger = setup_logger()

def main():
    logger.info("Starting the calculator application.")
    command_handler = CommandHandler()
    load_plugins(command_handler)  # Load plugins dynamically
    print("Welcome to the Advanced Calculator. Type 'help' for assistance, 'menu' to list commands, or 'exit' to quit.")

    while True:
        command_input = input(">>> ")
        if command_input.lower() == 'exit':
            logger.info("Exiting the calculator application.")
            print("Exiting calculator...")
            break
        elif command_input.lower() == 'help':
            print("Type any arithmetic command, or 'menu' to see a list of available commands, or 'exit' to close the application.")
        elif command_input.lower() == 'menu':
            print("Available commands:")
            for cmd in command_handler.commands.keys():
                print(cmd)
        else:
            try:
                output = command_handler.handle_command(command_input)
                print(f"Result: {output}")
            except Exception as e:
                logger.error(f"Error processing command: {e}")
                print(f"Error: {e}")

if __name__ == "__main__":
    main()