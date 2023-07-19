from pydantic_settings import BaseSettings
from starlette.config import Config

config = Config(".env")


class Settings(BaseSettings):
    DEBUG_KEY: str = config("DEBUG_KEY")  # TODO: Remove this

    # Azure Vision API Configration
    AZURE_VISION_PARAMS: dict = {
        "features": "read",
        "language": "ja",
    }
    AZURE_VISION_KEY: str = config("AZURE_VISION_KEY")
    AZURE_VISION_ENDPOINT: str = config("AZURE_VISION_ENDPOINT")
    AZURE_VISION_API_ENDPOINT: str = config("AZURE_VISION_API_ENDPOINT")

    # OpenAI Configration
    OPENAI_KEY: str = config("OPENAI_KEY")
    GPT_MODEL_NAME: str = config("GPT_MODEL_NAME")

    PROMPT_SYSTEM: str = "You are a program that classifies data from OCR receipts"
    PROMPT_ASSISTANT: str = "Classify the data of the receipts you are about to post in Japanese.\
        Types: 1=food, 2=drink, 3=ingredients, 9=alcohol/tobacco, 0=other. No extra explanation.\n"
    PROMPT_USER: str = "Convert the above receipt data into the same format as the sample below.\
        No extra explanation.\n\n"
    PROMPT_EXAMPLE: dict = {
        "store": {"name": "Name", "address": "Address", "telephone": "Phone"},
        "datetime": "2023-06-10T12:34:56",
        "items": [
            {"item_name": "Item1", "quantity": 1, "unit_price": 100, "type": 1},
            {"item_name": "Item2", "quantity": 2, "unit_price": 200, "type": 0},
        ],
        "tax": 50,
        "tax_included_price": 550,
    }

    # Database Configration
    DATABASE_HOST: str = config("DATABASE_HOST")
    DATABASE_USER: str = config("DATABASE_USER")
    DATABASE_PASSWORD: str = config("DATABASE_PASSWORD")
    DATABASE_NAME: str = config("DATABASE_NAME")
    DATABASE_PORT: str = config("DATABASE_PORT")


settings = Settings()
