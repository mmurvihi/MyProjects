# Write your code for every function
# Project 2 - Moonlander Functions
# Author: Margot Murvihill 
# Version: 

#The function show Welcome displays the welcome message at the beginning of the program.
def showWelcome():
   print('Welcome aboard the Lunar Module Flight Simulator')
   print ("\n"+"   To begin you must specify the LM's initial altitude")
   print ('   and fuel level.  To simulate the actual LM use')
   print  ('   values of 1300 meters and 500 liters, respectively.')
   print('\n'+'   Good luck and may the force be with you!')

#The function getFuel prompts the user to input the amount of fuel and returns an error 
#message if the number is not positive.     
def getFuel():
   fuelAmount=int(input('Enter the initial amount of fuel on board the LM (in liters): '))  
   while fuelAmount<=0:
      print('ERROR: Amount of fuel must be positive, please try again')
      fuelAmount=int(input('Enter the initial amount of fuel on board the LM (in liters):'))         
   return fuelAmount

#The function getAltitude prompts the user to enter a value in meters representing the 
#altitude and returns an error message if the number is not within 1-9999, inclusive.
def getAltitude():
   altitude=int(input('\n'+'Enter the initial altitude of the LM (in meters): '))
   while altitude<1 or altitude>9999:
      print('ERROR: Altitude must be between 1 and 9999, inclusive, please try again')
      altitude=int(input('Enter the initial altitude of the LM (in meters):'))
   return altitude

#The function displayLMState passes elapsedTime, altitude, velocity, fuelAmount, and fuelRate
#to display the state of the LM.
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):  
   print('Elapsed Time: {0:4} s'.format(elapsedTime))
   print('        Fuel: {0:4} l'.format(fuelAmount))
   print('        Rate: {0:4} l/s'.format(fuelRate))
   print('    Altitude: {0:7.2f} m'.format(altitude))
   print('    Velocity: {0:7.2f} m/s'.format(velocity))

#The function getFuelRate prompts the user to imput a fuel rate between 0-9 
#and returns an error message when the condition is not met.
def getFuelRate(currentFuel):
   FuelRate=int(input('\n'+'Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): '))
   while FuelRate<0 or FuelRate>9:
      print('ERROR: Fuel rate must be between 0 and 9, inclusive')
      FuelRate=int(input('Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust):'))
   return min(currentFuel, FuelRate)

#The function displayLMLandingStatus passes the velocity through the function
#and displays a message regarding the velocity at landing.
def displayLMLandingStatus(velocity):
   if velocity>=-1 and velocity<=0:
      print('\n'+'Status at landing - The eagle has landed!')
   elif velocity>=-10 and velocity<=-1:
      print('\n'+'Status at landing - Enjoy your oxygen while it lasts!')
   else:
      print('\n'+'Status at landing - Ouch - that hurt!') 

#The function updateAcceleration passes gravity and fuelRate to return the 
#updated acceleration. 
#float int -> int 
def updateAcceleration(gravity, fuelRate):
   acceleration=gravity*((fuelRate/5)-1)
   return acceleration    
	
#The function updateAltitude passes altitude, velocity, and acceleration to 
#return the udpated altitude. 
#float float float -> float
def updateAltitude(altitude, velocity, acceleration):
   altitude = altitude+velocity+(acceleration/2)
   if altitude <= 0:
      return 0
   else:
      return altitude 

#The function updateVelocity passes velocity and acceleration to return the 
#updated velocity.
#float float -> float
def updateVelocity(velocity, acceleration):
   velocity = velocity+acceleration
   return velocity 

#The function updateFuel passes fuel and fuelRate to return the updated fuel 
#rate. 
# int int -> int
def updateFuel(fuel, fuelRate):
   fuel = fuel-fuelRate
   return fuel

