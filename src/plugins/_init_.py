import os
import importlib.util

def load_plugins(command_handler):
    plugins_dir = os.path.dirname(__file__)
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]
            module_path = os.path.join(plugins_dir, filename)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, 'setup'):
                module.setup(command_handler)