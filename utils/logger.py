import logging
import pathlib

log_dir = pathlib.Path("logs")
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "test_execution.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)