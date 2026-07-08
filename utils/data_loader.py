import json
import logging
import os
from datetime import datetime

# Crear carpeta logs si no existe
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_filename = os.path.join(log_dir, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger()


def load_users_csv(path="data/users.csv"):
    import csv
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def read_products_json(path="data/products.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
