import os



CURRENT_DIR = os.path.abspath(__file__)
PARENT_DIR = os.path.dirname(CURRENT_DIR)
CY_DIR = os.path.dirname(PARENT_DIR)
PARENT_DIR = os.path.dirname(CY_DIR)
config_path = os.path.join(CY_DIR, "config", 'config.ini')
# print(self.config_path)
test = PARENT_DIR + '\cy\config\config.ini'



print(config_path)

print(test)