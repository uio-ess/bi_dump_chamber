#!/usr/bin/env python
import os
import epics
import time

# address of the machine running the IOC
IOC_IP = "172.30.150.81"
os.environ["EPICS_CA_ADDR_LIST"] = IOC_IP

# prints position for a number of seconds
def print_pos(t):
  t0 = time.time()
  dt = 0
  while (dt < t):
    pos = epics.caget(ax+'.RBV')
    print(f'Position = {pos} [mm]')
    time.sleep(0.2)
    dt = time.time() - t0


# axis pv name
ax = 'IOC2:Axis1'

# jog fwd
print('Jogging FWD')
epics.caput(ax+'.JOGF', 1)
print_pos(5)
epics.caput(ax+'.JOGF', 0)
print_pos(3)

# jog rev
print('Jogging REV')
epics.caput(ax+'.JOGR', 1)
print_pos(7)

# stop jog
print('Stop Jogging')
epics.caput(ax+'.JOGR', 0)

