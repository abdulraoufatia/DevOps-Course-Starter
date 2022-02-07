import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.API_KEY = os.environ.get("API_KEY")
        self.API_TOKEN = os.environ.get("API_TOKEN")
        self.BOARD = os.environ.get("BOARD")
        self.SECRET_KEY = os.environ.get("SECRET_KEY")
        if not self.SECRET_KEY:
            raise ValueError(
                "No SECRET_KEY set for Flask application. Did you follow the setup instructions?"
            )
