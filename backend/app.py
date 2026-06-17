from fastapi import FastAPI
import psycopg2

try:
    conn = psycopg2.connect (
        host='localhost',
        database='worldcup',
        user='postgres',
        password='IamThe_Best1'
    )
    print("Connection Successfull !!!!")
    conn.close()
except Exception as e :
    print(f'Error{e}')


app = FastAPI()

@app.get("/api/health")
def home():
    return{"status": "OK"}

@app.get("/api/standings")
def get_standing():
    teams = [
        {

            "id":1,
            "name": "India",
            "group": "A",
            "matches": 3,
            "wins": 2,
            "draws": 1,
            "losses": 0,
            "goalsFor": 8,
            "goalsAgainst": 2,
            "points": 7
        },
         {
            "id": 2,
            "name": "Argentina",
            "group": "A",
            "matches": 5,
            "wins": 4,
            "draws": 1,
            "losses": 0,
            "goalsFor": 12,
            "goalsAgainst": 3,
            "points": 13
        },
        {
            "id": 3,
            "name": "Senegal",
            "group": "A",
            "matches": 3,
            "wins": 1,
            "draws": 1,
            "losses": 1,
            "goalsFor": 4,
            "goalsAgainst": 4,
            "points": 4
        },
        {
            "id": 4,
            "name": "Qatar",
            "group": "A",
            "matches": 3,
            "wins": 0,
            "draws": 0,
            "losses": 3,
            "goalsFor": 1,
            "goalsAgainst": 8,
            "points": 0
        },
        {
            "id": 5,
            "name": "England",
            "group": "B",
            "matches": 3,
            "wins": 2,
            "draws": 1,
            "losses": 0,
            "goalsFor": 9,
            "goalsAgainst": 2,
            "points": 7
        },

        {
            "id": 6,
            "name": "USA",
            "group": "B",
            "matches": 3,
            "wins": 1,
            "draws": 2,
            "losses": 0,
            "goalsFor": 4,
            "goalsAgainst": 2,
            "points": 5
        },

         {
            "id": 7,
            "name": "Iran",
            "group": "B",
            "matches": 3,
            "wins": 1,
            "draws": 0,
            "losses": 2,
            "goalsFor": 3,
            "goalsAgainst": 6,
            "points": 3
        },
        {
            "id": 8,
            "name": "Wales",
            "group": "B",
            "matches": 3,
            "wins": 0,
            "draws": 1,
            "losses": 2,
            "goalsFor": 1,
            "goalsAgainst": 7,
            "points": 1
        }

    ]
    return{"standings": teams}

@app.get("/api/top-scorers")
def get_top_scorers():
    scorers = [
        {
            "id": 1,
            "player": "Kylian Mbappe",
            "country": "France",
            "matches": 7,
            "goals": 8,
            "assists": 2
        },
        {
            "id": 2,
            "player": "Lionel Messi",
            "country": "Argentina",
            "matches": 7,
            "goals": 7,
            "assists": 3
        },
        {
            "id": 3,
            "player": "Olivier Giroud",
            "country": "France",
            "matches": 6,
            "goals": 4,
            "assists": 1
        },
        {
            "id": 4,
            "player": "Julian Alvarez",
            "country": "Argentina",
            "matches": 7,
            "goals": 4,
            "assists": 1
        },
        {
            "id": 5,
            "player": "Richarlison",
            "country": "Brazil",
            "matches": 5,
            "goals": 3,
            "assists": 0
        },
        {
            "id": 6,
            "player": "Bukayo Saka",
            "country": "England",
            "matches": 4,
            "goals": 3,
            "assists": 1
        },
        {
            "id": 7,
            "player": "Marcus Rashford",
            "country": "England",
            "matches": 5,
            "goals": 3,
            "assists": 0
        },
        {
            "id": 8,
            "player": "Cody Gakpo",
            "country": "Netherlands",
            "matches": 5,
            "goals": 3,
            "assists": 0
        },
        {
            "id": 9,
            "player": "Bruno Fernandes",
            "country": "Portugal",
            "matches": 5,
            "goals": 2,
            "assists": 3
        },
        {
            "id": 10,
            "player": "Harry Kane",
            "country": "England",
            "matches": 5,
            "goals": 2,
            "assists": 3
        }
    ]
    return{"topScorers": scorers}

@app.get("/api/matches")
def get_matches():
    matches = [
        {
            "id": 1,
            "team1": "Argentina",
            "team2": "France",
            "score1": 3,
            "score2": 3,
            "status": "finished",
            "date": "2026-06-15"
        },
        {
            "id": 2,
            "team1": "Brazil",
            "team2": "Germany",
            "score1": 2,
            "score2": 1,
            "status": "finished",
            "date": "2026-06-14"
        },
        {
            "id": 3,
            "team1": "England",
            "team2": "Portugal",
            "score1": 1,
            "score2": 1,
            "status": "finished",
            "date": "2026-06-14"
        },
        {
            "id": 4,
            "team1": "Spain",
            "team2": "Netherlands",
            "score1": 0,
            "score2": 2,
            "status": "finished",
            "date": "2026-06-13"
        },
        {
            "id": 5,
            "team1": "Belgium",
            "team2": "Croatia",
            "score1": 2,
            "score2": 0,
            "status": "finished",
            "date": "2026-06-13"
        },
        {
            "id": 6,
            "team1": "Mexico",
            "team2": "USA",
            "score1": None,
            "score2": None,
            "status": "scheduled",
            "date": "2026-06-18"
        },
        {
            "id": 7,
            "team1": "Argentina",
            "team2": "Brazil",
            "score1": None,
            "score2": None,
            "status": "scheduled",
            "date": "2026-06-20"
        },
        {
            "id": 8,
            "team1": "France",
            "team2": "England",
            "score1": None,
            "score2": None,
            "status": "scheduled",
            "date": "2026-06-22"
        }
    ]
    return{"matches": matches}










