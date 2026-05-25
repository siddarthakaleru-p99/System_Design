import logging


class SingletonLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)

            cls._instance.logger = logging.getLogger("AppLogger")
            cls._instance.logger.setLevel(logging.INFO)

            if not cls._instance.logger.handlers:

                file_handler = logging.FileHandler("app.log")
                file_handler.setLevel(logging.INFO)

                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.INFO)

                formatter = logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(message)s"
                )

                file_handler.setFormatter(formatter)
                console_handler.setFormatter(formatter)

                cls._instance.logger.addHandler(file_handler)
                cls._instance.logger.addHandler(console_handler)

        return cls._instance

    def get_logger(self):
        return self.logger