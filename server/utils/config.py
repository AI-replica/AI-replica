import os
from server.utils.read_config import config

STATIC_FILES_DIR = config["server"]["static_files_dir"]
GENERATED_FILES_DIR = os.path.join(STATIC_FILES_DIR, "generated")
