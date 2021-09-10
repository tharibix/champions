import requests, pandas as pd
from bs4 import BeautifulSoup


html_doc = requests.get('https://es.uefa.com/uefachampionsleague/standings/')
soup = BeautifulSoup(html_doc.text, 'html.parser')


num = 199
divs = []
rows = []
data = []

TITLE = ''' 

               ~ TABLAS OFICIALES DE LA UEFA CHAMPIONS LEAGUE ~
            
            by: tharibix



            '''

for _ in range(8):


    for i in range(1,5):
            
        # main div
        code = "grp-2008" + str(num)
        div = soup.find(id=code)
    
        # Group name 
        group_name = div.find('span', {'class': 'group-name'})
        gp_name = str(group_name.text)
        gpname = gp_name.replace('\r\n', "")
        divs.append(gpname.strip())
   

        # Filas de equipos (ranking) and info
        tr = div.select(f'tr[data-rank="{i}"] ')

        for team in tr:
        
            del_span = team.find('span', attrs={"class": "now-playing_label"}).decompose()
        
            team_name = team.find('span', attrs={"class": "team-name js-team-name"}).text.strip()

            pj = team.find('td', attrs={"class": "table_team-played js-played"}).text.strip()
            pg = team.find('td', attrs={"class": "table_team-won js-won"}).text.strip()
            pe = team.find('td', attrs={"class": "table_team-drawn js-drawn"}).text.strip()
            pp = team.find('td', attrs={"class": "table_team-lost js-lost"}).text.strip()
            af = team.find('td', attrs={"class": "table_team-for js-goalsFor"}).text.strip()
            ec = team.find('td', attrs={"class": "table_team-against js-goalsAgainst"}).text.strip()
            dg = team.find('td', attrs={"class": "table_team-goal-diff js-goalDifference"}).text.strip()
            pts = team.find('strong', attrs={"class": "js-points"}).text.strip()


            team_row = {
                'Grupo': gpname,
                'Team': team_name,
                'Partidos': pj,
                'Victorias': pg, 
                'Empates': pe, 
                'Derrotas': pp, 
                'A favor': af, 
                'En contra': ec, 
                'Diferencia de goles': dg, 
                'Puntos': pts
            }

            data.append(team_row)

    num+=1  # Aumenta la cuenta del numero final del id del div para que haga match al concatenarlo.



print(TITLE)

teams_info = pd.DataFrame(data)

print(teams_info)

    



    




