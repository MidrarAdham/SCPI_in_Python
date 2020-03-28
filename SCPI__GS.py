import socket

#example python script for GS communication
#establishing connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(1)
s.connect(('192.168.0.149',5025))

# why do we need to lock out screen?
# sending lock screen cmnd (lock screen)
output = 'SYST:RWL\n'
s.send(output.encode('utf-8'))



#sending desired command
#send IDN QUERY for example
output1 = '*IDN?\n'
s.send(output1.encode('utf-8'))
msg = s.recv(1024).decode()
print('Module id,Serial num, Firmware rev',msg)

# Change the output voltage

#output2 = 'VOLTage 208'
#s.send(output2.encode('utf-8'))

output3 = 'CONFigure:HW:MODE?\n'
s.send(output3.encode('utf-8'))
msg1 = s.recv(1024)
print('Mode number: ',msg1.decode('ascii'))

#Measure the output voltage

output4 = 'MEASure:VOLTage?\n'
s.send(output4.encode('utf-8'))
msg1 = s.recv(1024)
print('Output Voltage is: ',msg1.decode('ascii'),'volts')
 
#output5 = '*ESR?\n'   
#s.send(output4.encode('utf-8'))
#msg1 = s.recv(1024)
#print('esr = ',msg1.decode('ascii'))



# return screen to local control (unlock screen)
output5 = 'SYST:LOC\n'
s.send(output5.encode('utf-8'))
# close connection
s.close()