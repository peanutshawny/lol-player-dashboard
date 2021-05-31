import mysql.connector
from db_creds import host, user, passwd, database

# connecting to database
db = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    database=database
)

lol_cursor = db.cursor()

lol_cursor.execute('select * from champion')
champs = lol_cursor.fetchall()

for champ in champs:
    print(champ)

# test = lol_cursor.execute('''
# SELECT
#
#   game_instance.Win,
#   champion.Name
#
# FROM game_instance
#
#   INNER JOIN game_champ ON game_instance.GameID = game_champ.GameID
#   INNER JOIN champion ON game_champ.ChampionID = champion.ID
#
# WHERE champion.name = "Ashe";
# '''
# ).fetchone()[0]