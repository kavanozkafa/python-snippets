import sys #system library. command,input,output vs.

sys.stderr.write('stderr test\n') #for errors
sys.stderr.flush() 
sys.stdout.write('stdout test\n') #for outputs

print(sys.argv) # file path or file name.basically all the arguments you pass
#if you run this print(sys.argv) on terminal you'll get filename
#if you run it on ide or text editor you'll get file path
#or if you execute this command #python3 sys_Module.py "pass me to"
#you'll get ['sys_Module.py', 'pass me to']
#sys modülünün argv niteliği, yazdığımız program çalıştırılırken kullanılan parametreleri bir liste halinde tutar.


sys.exit() # stop the program.sys modülünün exit() fonksiyonunu kullanarak, programınızın işleyişini durdurabilir, programınızı kapanmaya zorlayabilirsiniz

sys.getwindowsversion() #Windows sürümüne ilişkin bilgi verir








#for more visit : https://docs.python.org/3/library/sys.html