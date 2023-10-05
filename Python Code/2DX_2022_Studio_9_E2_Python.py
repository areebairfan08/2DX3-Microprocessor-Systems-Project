# Modify the following line with your own serial port details
#   Currently set COM3 as serial port at 115.2kbps 8N1
#   Refer to PySerial API for other options.  One option to consider is
#   the "timeout" - allowing the program to proceed if after a defined
#   timeout period.  The default = 0, which means wait forever.


#Areeba Irfan  - 400378045 - irfana20

import serial
import math

s = serial.Serial('COM3',115200)

s.open

# reset the buffers of the UART port to delete the remainin data in the buffers
s.reset_output_buffer()
s.reset_input_buffer()

rotations = int(input("enter number of rotations:"))
counter = 0 #variable to keep track of how many rotations have happened

motor_steps = 0 #steps for motor up to 512 for 360 deg

x_coord = 0 #for every 360 deg, x will increase
increase = 200 # increase x displacement by 200 each rotation

f = open("data_points.xyz", "w")

while(counter<rotations):
    
    x = s.readline()
    point = x.decode("utf-8") # Decodes byte input from UART into string 
    point = point[0:-2] #extract the points
    
    if (point.isdigit() == True): #start the calculations in the data is a number (so it doesnt accidently start at the initalizing messaes 
        
        angle = (motor_steps/512)*2*math.pi #calculation for the angle
        hyp = int(point)
        y = hyp*math.cos(angle) 
        z = hyp*math.sin(angle) 
        
        f.write('{} {} {}\n'.format(x_coord,y,z)) #write the points to an xyz file
        
        motor_steps = motor_steps+32 #increases the angle by 22.5
        
    if (motor_steps == 512): #when a full rotation has occured
        motor_steps = 0 #reset
        x_coord = x_coord + increase #increase the displacement
        counter=counter+1 #increase the counter
        
    print(point)# print the point
    
f.close() #close file when done so data saves
