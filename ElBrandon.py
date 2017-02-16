counter=0
teams = []
while(counter<5):
    team = input ("Nombre equipos campeones ")
    #Agrega cada ingreso a la lista
    teams.append(team)
    counter = counter+1
#Se muestran los 5 equipos
for team in teams:
    print(f"{team}")
#Ce fini!
