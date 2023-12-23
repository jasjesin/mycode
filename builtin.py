import os      # to fetch OS-specific details
import logging # to log error or debug msgs for testing

print(os.name)

logger = logging.getLogger("MAIN")
logger.error("Error happened in builtin app")

