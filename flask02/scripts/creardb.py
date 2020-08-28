import os,sys
sys.path.append(os.getcwd())
from app import db
import models

db.create_all()