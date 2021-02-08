# files to ship
# -> main.py
# -> config.ini
# -> hydro.db

from datetime import datetime
from configparser import ConfigParser
import serial
import time
import multiprocessing
import sqlite3 


class Hydro:
    def __init__(self):

        self.file = 'config.ini'
        self.cfg = ConfigParser()
        self.cfg.read(self.file)
        

        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.pump_on_time = self.cfg['intervals']['pump_on']
        self.pump_off_time = self.cfg['intervals']['pump_off']
        self.pump_is_on = False

        self.conn = sqlite3.connect('dat_col.db')
        self.c = self.conn.cursor()

    
    def pump_on(self):
        time.sleep(0.1)
        self.ser.write(b'H')

        self.cfg.set('temp', 'pump_is_on', '1')
        with open(self.file, 'w') as self.cfgfile:
            self.cfg.write(self.cfgfile)
            print('WRITTEN: pump_is_on = 1')

        self.pump_is_on = True
        return(self.pump_is_on)


    def pump_off(self):
        time.sleep(0.1)
        self.ser.write(b'L')

        self.cfg.set('temp', 'pump_is_on', '0')
        with open(self.file, 'w') as self.cfgfile:
            self.cfg.write(self.cfgfile)
            print('WRITTEN: pump_is_on = 0')
        
        self.pump_is_on = False
        return(self.pump_is_on)

    def pump_cycle(self):
        while True:
            self.pump_on()
            time.sleep(int(self.pump_on_time))
            self.pump_off()
            time.sleep(int(self.pump_off_time))

    def dat_col(self):
        self.pump_store = self.cfg['temp']['pump_is_on']
        self.light_store = self.cfg['temp']['light_is_on']
        self.now = datetime.now()
        
        self.photoid = 2

        self.c.execute("INSERT INTO data VALUES ('{}', '{}', '{}', '{}')".format(self.now, self.photoid, self.pump_store, self.light_store))
        self.conn.commit()
        # datetime, photoid, is_pump_on, is_light_on, 

        #self.c.execute("SELECT * FROM data WHERE photoid = '1'")
        #return print(self.c.fetchall()) 

    def read_dat(self):
        self.c.execute("SELECT * FROM data WHERE photoid = '2'")
        return self.c.fetchone()
    

hydro = Hydro()

time.sleep(2)


#print(hydro.dat_col())
print(hydro.read_dat())










#print('Pump on interval = ' + str(hydro.pump_on_time + ' sec(s)'))
#print('Pump on interval = ' + str(hydro.pump_off_time + ' sec(s)'))
#print('\n')





#file = 'config.ini'
#cfg = ConfigParser()
#cfg.read(file)


#cfg.set('temp', 'pump_is_on', '0')

#with open(file, 'w') as cfgfile:
    #cfg.write(cfgfile)


#p_pump_cycle = multiprocessing.Process(target=hydro.pump_cycle)
#p_pump_cycle.start()



#hydro.pump_off()

#def pp():
#    ser = serial.Serial('/dev/ttyACM0', 9600)
#    time.sleep(0.1)
#    ser.write(b'L')
#    ser.close()
#pp()
