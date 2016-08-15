import telnetlib,time,sys
def conn(x):
  T=telnetlib.Telnet
  user='admin'  
  pw='password'   
  tl=T(x)

  tl.read_until('Username:')
  tl.write(user+'\n')

  tl.read_until('Password:')
  tl.write(pw+'\n')
  
  print 'hi'
  tl.read_until('>')
  tl.write('system-view'+'\n')  
#  cmd=['local-user admin','password cipher jxa618a']
  
  print 'hi'
  tl.read_until(']')
  tl.write('local-user admin2132'+'\n')
 
  print 'hi'
  tl.read_until(']')
  tl.write('password cipher jxa618a'+'\n')
  
  tl.read_until(']')
  tl.write('service-type telnet level 3'+'\n')

  print tl.read_until(']')
  print 'hi'
  tl.write('sa'+'\n') 
  tl.write('y'+'\n')
  tl.write('\n')
#  tl.read_all()    
  print tl.read_very_eager()
  tl.close()
f=open('ip.txt','r')
for ip in f:
  ip = ip.strip('\n')   
  print ip 
  conn(ip)
