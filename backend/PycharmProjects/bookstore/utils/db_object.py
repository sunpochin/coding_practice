from databases import Database
from utils.const import *

if TESTING:
    print("TEST_DB_URL: ", TEST_DB_URL)
    db = Database(TEST_DB_URL)
else:
    db = Database(DB_URL)
