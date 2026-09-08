import json
import logging
from pathlib import Path

class JsonFormatter(logging.Formatter):
    def format(self, record) -> str:
        log_record = {
            'ts': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'msg': record.getMessage(),
            'logger': record.name
        }
        return json.dumps(log_record)

def get_logger(name="pipeline", log_path="logs/pipeline.log") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    Path(log_path).parent.mkdir(parents=True, exist_ok=True)

    filehandler = logging.FileHandler(log_path)
    filehandler.setFormatter(JsonFormatter())
    logger.addHandler(filehandler)

    return logger