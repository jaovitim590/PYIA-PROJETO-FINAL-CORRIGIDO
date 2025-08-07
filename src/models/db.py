import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def get_db():
  return mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
  )

