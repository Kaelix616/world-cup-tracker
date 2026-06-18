import psycopg2
class Database:
    def __init__(self):
        try: 
            self.conn=psycopg2.connect(
                host='localhost',
                database='worldcup',
                user='postgres',
                password='IamThe_Best1'
            )
            self.cursor=self.conn.cursor()
            print("CONNECTION SUCCESSFULL !!!")
            
        except Exception as e:
            print(f'message{e}')

    def create_tables(self):
        try:
            # teams table
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS teams(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) UNIQUE,
                    team_group VARCHAR(10),
                    matches INT DEFAULT 0,
                    wins INT DEFAULT 0,
                    draws INT DEFAULT 0,
                    losses INT DEFAULT 0,
                    goals_for INT DEFAULT 0,
                    goals_against INT DEFAULT 0,
                    points INT DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )

            ''')

            # players table
            self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS players (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(100),
                            team_id INT REFERENCES teams(id),
                            goals INT DEFAULT 0,
                            assists INT DEFAULT 0,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

                                )                    
                ''')

           # matches table 
            self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS matches (
                            id SERIAL PRIMARY KEY,
                            team1_id INT REFERENCES teams(id),
                            team2_id INT REFERENCES teams(id),
                            team1_goals INT,
                            team2_goals INT,
                            status VARCHAR(20),
                            matches_date TIMESTAMP,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                )

                ''')
            
            self.conn.commit()
            print("ALL TABLE CREATED SUCCESSFULLY!!!!")
        except Exception as e:
            print(f'ERROR creating table {e}')
            self.conn.rollback()


    def insert_sample_data(self):
        try:
            teams_data = [
                ('India', 'A', 3,2,1,0,8,2,7),
                ('Argentina', 'A',5,4,1,0,12,3,13),
                
                ('Senegal','A',3,1,1,1,4,4,4),
                ('Qatar','A',3,0,0,3,1,8,0),
                ('England','B',3,2,1,0,9,2,7)
            ]

            #data in tha table: 
            for team in teams_data:
                self.cursor.execute('''
                    INSERT INTO teams(name,team_group,matches,wins,draws,losses,goals_for,goals_against,points)
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    

                ''',team)

            #playar data:
            players_data=[
                ('Kylian Mbappe',1,8,2,),
                ('Lionel Messi',2,7,3),
                ('Neymar',5,5,2),
                ('Harry Kane',4,6,1)
            ]

            #data in table: 
            for player in players_data:
                self.cursor.execute('''
                    INSERT INTO players(name,team_id,goals,assists)
                    VALUES(%s,%s,%s,%s)    
                ''',player)


            #matches data:
            matches_data=[
                (1,2,3,3,'finished','2026-06-15'),
                (3,4,2,1,'finished','2026-06-13'),
                (4,5,1,1,'finished','2026-06-014')
            ]

            for match in matches_data:
                self.cursor.execute('''
                        INSERT INTO matches(team1_id,team2_id,team1_goals,team2_goals,status,matches_date)
                        VALUES(%s,%s,%s,%s,%s,%s)  
                        ''',match)
            self.conn.commit()
            print("Data inserted successfully")
        except Exception as e:
            print(f'Error inserting data{e}')

    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Connection CLOSED ")

if __name__=="__main__":
    db = Database()
    db.create_tables()
    db.insert_sample_data()
    db.close()

