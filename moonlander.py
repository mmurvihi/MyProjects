#Margot Murvihill
#Sussan Einakian
#CPE 101 Section 1

import landerFuncs

elapsedTime = fuelRate = velocity = acceleration = 0
gravity = 1.62

landerFuncs.showWelcome()
altitude = landerFuncs.getAltitude()
fuel = fuelAmount = currentFuel = landerFuncs.getFuel()
print('\n'+'LM state at retrorocket cutoff')
landerFuncs.displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
while altitude > 0 and fuelAmount > 0:
   fuelRate = landerFuncs.getFuelRate(currentFuel)
   fuel = currentFuel = fuelAmount = landerFuncs.updateFuel(fuel, fuelRate)
   acceleration = landerFuncs.updateAcceleration(gravity, fuelRate)
   altitude = landerFuncs.updateAltitude(altitude, velocity, acceleration)
   velocity = landerFuncs.updateVelocity(velocity, acceleration)
   elapsedTime += 1
   if altitude > 0 and fuelAmount > 0:
      landerFuncs.displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)

while fuelAmount == 0 and altitude > 0:
   print('OUT OF FUEL - Elapsed Time: {0:3} Altitude: {1:7.2f} Velocity: {2:7.2f}'.format(elapsedTime, altitude, velocity))
   fuelRate = 0
   fuel = currentfuel = fuelAmount = landerFuncs.updateFuel(fuel, fuelRate)
   acceleration = landerFuncs.updateAcceleration(gravity, fuelRate)
   altitude = landerFuncs.updateAltitude(altitude, velocity, acceleration)
   velocity = landerFuncs.updateVelocity(velocity, acceleration)
   elapsedTime += 1

print('\n'+'LM state at landing/impact')
landerFuncs.displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
landerFuncs.displayLMLandingStatus(velocity)
