# import the libraries
from urllib.request import urlopen
import json

#Reading the json file and creating the variables to work with
file = urlopen("https://data.transportation.gov/resource/4f3n-jbg2.json?year=2021")
data = json.loads(file.read())
jsonFormatted = json.dumps(data, indent=4)

#Input for departure and arrival city
city1 = input("Enter departure city: ")
city2 = input("Enter arival city: ")

#Main function 
def main():
    input1 = input("Are you looking for a direct flight? (Y/N): ")
    if input1 == 'Y' or input1 == 'y':
        directFlights()
    else:
        nonDirectFlights()

#If user wants a direct flight, this functiomn will execute
def directFlights():
    print("Flights and Prices")
    print("------------------")
    #Logic to get the direct flights and match them
    for x in range(len(data)):
        if city1 == data[x]["city1"] and city2 == data[x]["city2"]:
            fare = "${:,.2f}".format(float(data[x]["fare"]))
            print(f'Flight #{x}: {city1} -> {city2} = {fare}')
            
#If user wants a non direct flight or thir direct flight isnt available, this functiomn will execute
def nonDirectFlights():
    visited = []
    visited2 = []
    #Putting all the departure city flights into a list
    for x in range(len(data)):
        if city1 in data[x]["city1"]:
            visited.append(data[x])
            print(f'Flight -> {visited.sort}')
    #Logic to match the flight 1 city 2 with flight 2 city 1 data to get the connecting flights
    while visited:
        flight1 = visited.pop()
        visited2.append(flight1)
        if city2 in flight1["city2"]:
            print(flight1)
        for flight2 in data:
            if flight2["city1"] == flight1["city2"] and flight2 not in visited2:
                visited.append(flight2)
            
main()






    


   








