#General Practice
name = "Francis"
last = "Mangala"
age = 36
wage=23
dailyw= wage*8
print( f"My name is {name} and I make {dailyw} per day. On top of that I am {age} years old")

#Creating a list

DRCongo = ["Kinshasa", "Mbandaka","Goma","Mbuji-Mayi","Gemena","Lubumbashi","Matadi","Ilebo","Kalemie"]
cities2=["Lisala","Kikwit","Gungu","Bukavu","Beni"]

City_list=list(DRCongo)

#Extend will attach only elements of the list
City_list.extend(cities2)

#Append will attach the list a a whole
print(City_list)

CityNumber= len(City_list)

#To store data
tuple(City_list)

print(CityNumber)

#Create a Dictionary (keys, values)
CityIndex= {}
CityIndex["Kinshasa"]=445891
CityIndex["Mbandaka"]= 463353
CityIndex["Ilebo"]= 138224
CityIndex["Goma"]= 445441
CityIndex["Lisala"]= 223456
print(CityIndex)
print(CityIndex.keys())

#Using the IF function :

if "Kinshasa" in City_list:
    print("We are on the right track")
#To print keys and values from a dictionary
for County, Population in CityIndex.items():
    print(County,Population)

#To Import a file and read it on python

#Direct Path

import csv
import os

DataMovie = os.path.join("Data","netflix_ratings.csv")

with open(DataMovie) as Netflix_Movies:

    csv_reader = csv.reader(Netflix_Movies)

    headers = next(csv_reader)
    print(headers)