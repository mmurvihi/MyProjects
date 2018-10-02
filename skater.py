import math
from funcs import *


def main():
#Define the variables needed to calculate the velocity of the skater (mass of the skater, velocity 
#of the object, and mass of the object) by passing the inputs through our functions poundsToKG1, 
#getVelocityObject, and getMassObject. 
   mass_s = poundsToKG1(float(input('How much do you weigh (pounds)? ')))
   vel_o = getVelocityObject(float(input('How far away is your professor (meters)? ')))
   mass_o = getMassObject(input('Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? '))

#Return different messages to the user based on the mass and distance of the object.   
   if mass_o<=0.1:
      print ("\n"+"Nice throw! You're going to get an F!")
   elif mass_o>0.1 and mass_o<=1.0:
      print ('\n'+'Nice throw! Make sure your professor is OK.')
   elif mass_o>1 and vel_o<9.8994949366:
      print('\n'+'Nice throw! How far away is the hospital?')
   else:
      print('\n'+'Nice Throw! RIP professor.')


#Calculate and return the velocity of the skater based on the mass of the skater, mass of the
#object, and velocity of the object rounded to 3 decimal places with the unit m/s.
   vel_s = getVelocitySkater(mass_s, mass_o, vel_o)
   print ('Velocity of skater: %.3f m/s '%(vel_s)) 


#Return a message based on the velocity of the skater.
   if vel_s<0.2:
      print('My grandmother skates faster than you!')
   elif vel_s>=0.2 and vel_s<1.0:
      print(' ')
   else: 
      print('Look out for that railing!!!')

if __name__=='__main__':
   main()
