#!/usr/bin/env python
import os
import epics
import time
import logging

# https://epics.anl.gov/bcda/synApps/motor/R6-5/motorRecord.html

logging.basicConfig(format='%(asctime)s-%(levelname)s: %(message)s', level=logging.DEBUG)

# address of the machine running the IOC
ioc_user = "iocuser"
IOC_IP = "bd-cpu14.cslab.esss.lu.se"
os.environ["EPICS_CA_ADDR_LIST"] = IOC_IP

# some PV names:
pvbn = 'IOC2:'
ax = pvbn + 'Axis1'
rdy = pvbn + 'ready'

# check that the IOC is ready
ready_timeout = 10
t0 = time.time()
dt = 0
ready = False
logging.info("Checking if IOC is up...")
while (dt < ready_timeout) and (ready == False):
  if (epics.caget(rdy) == 1):
    ready = True
  dt = time.time() - t0
logging.info("It's up!")

if (ready == False):
  logging.warning(f"Try starting the IOC with `ssh {ioc_user}@{IOC_IP} /home/{ioc_user}/ecmctraining/run_this.sh`")
  raise Exception("IOC is not ready.")

def get_pos():
  return(epics.caget(ax+'.RBV'))

# prints position for a number of seconds
def print_pos(t, p=0.2):
  t0 = time.time()
  dt = 0
  while True:
    logging.debug(f'Position = {get_pos()} [mm]')
    dt = time.time() - t0
    if (dt < t):
      time.sleep(p)
    else:
      break

def goto(position, block=True, update_period=0.2):
  logging.info(f'Going to {position} [mm]...')
  epics.caput(ax+'.VAL', position)
  if (block == True):
    while moving():
      if (update_period == 0):
        pass
      else:
        print_pos(0)
        time.sleep(update_period)
    logging.info('Arrived!')

def jog(forward=True, duration=1.0, update_period=0.2):
  if (moving()):
    logging.warning("Can not initiate jog while the motor is moving.")
    return
  if (forward == True):
    txt = 'FWD'
    d = 'F'
  elif (forward == False):
    txt = 'REV'
    d = 'R'
  else:
    logging.warning("Bad jog direction.")
    return
  logging.info(f'Jogging {txt} for {duration}s...')
  epics.caput(ax+'.JOG'+d, 1)
  if update_period > 0:
    print_pos(duration, p=update_period)
  else:
    time.sleep(duration)
  epics.caput(ax+'.JOG'+d, 0) # stop jogging
  while moving(): pass
  logging.info(f'Jogging complete')

# stops the motor's motion
def stop():
  epics.caput(ax+'.STOP', 1)

# pauses the motor's motion
def pause():
  epics.caput(ax+'.STOP', 1)

# unpause the motor's motion
def unpause():
  epics.caput(ax+'.STOP', 2)

# disable pause mode
def no_pause():
  epics.caput(ax+'.SPMG', 3)

# returns true if the motor is in motion
def moving():
  #done_moving_flag = epics.caget(ax+'.DMOV') == 1
  #movement_in_progress_flag = epics.caget(ax+'.MIP') == 1
  #return (not done_moving_flag) or (movement_in_progress_flag)
  return (not (epics.caget(ax+'.DMOV') == 1))

#def get_motor_status():

initial_position = get_pos()
logging.info(f"Initial position: {initial_position} [mm]")


# jog fwd
jog(forward=True, duration=5)

# jog rev
jog(forward=True, duration=7)

# goto an exact position
goto(2.0)

goto(0.0, block=False)

while moving(): pass
final_position = get_pos()
logging.info(f"Final position: {final_position} [mm]")

logging.debug("Done")