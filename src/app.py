from flask import Flask
from database import InMemoryDatabase

app = Flask(__name__)
db = InMemoryDatabase()