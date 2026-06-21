from fastapi import FastAPI

from models import Database





app = FastAPI()

@app.get("/api/health")
def home():
    return{"status": "OK"}

@app.get("/api/standings")
def get_standing():
    db = Database()
    cursor=db.cursor
    cursor.execute("SELECT * FROM teams")
    result=cursor.fetchall()
    db.close
    return{"standings": result}

@app.get("/api/top-scorers")
def get_top_scorers():
    db=Database()
    cursor=db.cursor
    cursor.execute("SELECT * FROM players")
    result=cursor.fetchall()
    db.close
    return{"topScorers": result}

@app.get("/api/matches")
def get_matches():
    db=Database()
    cursor=db.cursor
    cursor.execute("SELECT * FROM matches")
    result=cursor.fetchall()
    db.close
    return{"matches": result}










