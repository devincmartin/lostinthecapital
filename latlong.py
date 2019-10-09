#EXTRA CREDIT
# Capitol Maps: Find your way around D.C.!
latitude = float(input("Insert your latitude: ")) 
longitude = float(input("Insert your longitude: "))

#Places: Latiitude
K_Street_Lat = 38.902649
White_House_Lat = 38.897789 
Downing_Hall_Lat = 38.921669
Dupont_Circle_Lat = 38.909760
Union_Station_Lat = 38.897698
greene_stadium_Lat = 38.928718
columbia_heights_Lat = 38.925600
potomac_Lat = 38.881501
farragut_Lat = 38.901212

#Places: Longitude
White_House_Long = -77.036562
Downing_Hall_Long = -77.021361
Dupont_Circle_Long = -77.043479
Union_Station_Long = -77.007200
greene_stadium_Long = -77.032442
columbia_heights__Long = -77.021200
potomac_Long = -76.985253
farragut_Long = -77.039223


#K Street 
if(latitude < K_Street_Lat):
    print("You are south of K St")
if(latitude > K_Street_Lat):
    print("You are north of K St")
    
#White House 
if(latitude < White_House_Lat):
    print("You are south of the White House")
if(latitude > White_House_Lat):
    print("You are north of the White House")
if(longitude < White_House_Long):
    print("You are west of the White House")
if(longitude > White_House_Long):
    print("You are east of the White House")
    
#Downing Hall 
if(latitude < Downing_Hall_Lat):
    print("You are south of Downing Hall")
if(latitude > Downing_Hall_Lat):
    print("You are north of Downing Hall")
if(longitude < Downing_Hall_Long):
    print("You are west of Downing Hall")
if(longitude > Downing_Hall_Long):
    print("You are east of Downing Hall")
    
#Dupoint Circle 
if(latitude < Dupont_Circle_Lat):
    print("You are south of Dupont Circle")
if(latitude > Dupont_Circle_Lat):
    print("You are north of Dupont Circle")
if(longitude < Dupont_Circle_Long):
    print("You are west of Dupont Circle")
if(longitude > Dupont_Circle_Long):
    print("You are east of Dupont Circle")

#Union Station 
if(latitude < Union_Station_Lat):
    print("You are south of Union Station")
if(latitude > Union_Station_Lat):
    print("You are north of Union Station")
if(longitude < Union_Station_Long):
    print("You are west of Union Station")
if(longitude > Union_Station_Long):
    print("You are east of Union Station")
    
    
#Green Stadium
G = "You are 0.8 miles from Downing Hall"
if float(round(latitude, 2)) == float(round(greene_stadium_Lat, 2)) and float(round(longitude, 2)) == float(round(greene_stadium_Long, 2)):
    print(G)
    
P = "You are 3.4 miles from Downing Hall"
if float(round(latitude, 2)) == float(round(potomac_Lat, 2)) and float(round(longitude, 2)) == float(round(potomac_Long, 2)):
    print(P)
    
F = "You are 1.8 miles from Downing Hall"
if float(round(latitude, 2)) == float(round(farragut_Lat, 2)) and float(round(longitude, 2)) == float(round(farragut_Long, 2)):
    print(F)



    
