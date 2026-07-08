import requests

from models import Database

class WorldCupScraper:
    def __init__(self):
        self.db = Database()  
        self.url = "https://worldcup26.ir/get/groups"

    def fetch_page(self):
        try:
            groups_url = "https://worldcup26.ir/get/groups"
            groups_response = requests.get(groups_url, timeout=10)
            groups_data = groups_response.json()
            
            teams_url = "https://worldcup26.ir/get/teams"
            teams_response = requests.get(teams_url, timeout=10)
            teams_data = teams_response.json()
            
            # DEBUG: Print first team
           
            
            print("✅ Data fetched successfully!")
            return {
                'groups': groups_data.get('groups', []),
                'teams': teams_data.get('teams', [])
            }
        except Exception as e:
            print(f'❌ Error fetching: {e}')
            return None
        
        
    
    def parse_teams(self, data):
        try:
            teams_data = []
            
            # Create team ID to name mapping
            team_map = {}
            for team in data.get('teams', []):
                team_map[team['id']] = team['name_en']  # ← Use 'id' and 'name_en'
            
            if 'groups' not in data:
                return []
            
            for group in data['groups']:
                for team in group['teams']:
                    team_obj = {
                        'name': team_map.get(team['team_id'], 'Unknown'),
                        'gp': int(team.get('mp', 0)),
                        'wins': int(team.get('w', 0)),
                        'draws': int(team.get('d', 0)),
                        'losses': int(team.get('l', 0)),
                        'goals_for': int(team.get('gf', 0)),
                        'goals_against': int(team.get('ga', 0)),
                        'points': int(team.get('pts', 0))
                    }
                    teams_data.append(team_obj)
            
            print(f"✅ Parsed {len(teams_data)} teams!")
            return teams_data
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
            return []


        
    
    def save_to_db(self, teams):
        try:
        
            for team in teams:
            
                self.db.cursor.execute('''
                    INSERT INTO teams 
                    (name, matches, wins, draws, losses, goals_for, goals_against, points)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (name) DO UPDATE SET
                        matches = EXCLUDED.matches,
                        wins = EXCLUDED.wins,
                        draws = EXCLUDED.draws,
                        losses = EXCLUDED.losses,
                        goals_for = EXCLUDED.goals_for,
                        goals_against = EXCLUDED.goals_against,
                        points = EXCLUDED.points
                ''', (
                    team['name'],
                    team['gp'],
                    team['wins'],
                    team['draws'],
                    team['losses'],
                    team['goals_for'],
                    team['goals_against'],
                    team['points']
                ))
        
            self.db.conn.commit()
            print(f"✅ {len(teams)} teams saved to database!")
        except Exception as e:
            print(f"❌ Error saving to database: {e}")
            self.db.conn.rollback()
    
    def run(self):
        print("🚀 Starting World Cup scraper...")
        
        
        data = self.fetch_page()
        if not data:
            return
        

        teams = self.parse_teams(data)
        if not teams:
            return
        
        self.save_to_db(teams)
        

        self.db.close()
        print("✅ Scraper finished!")


if __name__=="__main__":
    scraper = WorldCupScraper()
    scraper.run()



