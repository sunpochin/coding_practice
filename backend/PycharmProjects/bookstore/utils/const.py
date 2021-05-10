# generated using openssl rand -hex 32
JWT_SECRET_KEY = "e27a0ad8c442149f117cf188dfd3a6525436c9824a829903405605077ede42f1"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_TIME_MINUTES = 60 * 24 * 5

TOKEN_DESCRIPTION = "It check username and password"
TOKEN_SUMMARY = "It returns JWT token."

ISBN_DESCRIPTION = "It is unique identifier for books."
ISBN_SUMMARY = "ISBN summary."

DB_HOST = "165.232.145.210"
DB_USER = "admin"
DB_PASSWORD = "admin"
DB_NAME = "bookstore"

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
