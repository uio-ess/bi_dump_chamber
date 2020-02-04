#!/usr/bin/env python
import os
import epics
import time
import logging

# https://epics.anl.gov/bcda/synApps/motor/R6-5/motorRecord.html

logging.basicConfig(format='%(asctime)s-%(levelname)s: %(message)s', level=logging.DEBUG)

# address of the machine running the IOC
ioc_user = "iocuser"
#IOC_IP = "bd-cpu14.cslab.esss.lu.se"
IOC_IP = "10.41.0.165"
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
  epics.caput(ax+'.SPMG', 1)

# unpause the motor's motion
def unpause():
  epics.caput(ax+'.SPMG', 2)
  
# return the jog velocity setpoint
def get_jog_rate():
  jrate = epics.caget(ax+'.JVEL')
  logging.info(f'The jog step rate is {jrate/1000} [kHz] (maximum might be 128)')
  logging.info(f'or {jrate/200/60} motor RPM')
  logging.info(f'or {jrate/200/60/16} leadscrew RPM')
  logging.info(f'or {jrate/200/16/2.54} mm/sec (maximum might be 95.25)')
  return(jrate)

# return VELO
def get_speed():
  velo = epics.caget(ax+'.VELO')
  logging.info(f'VELO is {velo} [mm/sec]')
  return(velo)

# set the jog velocity
def set_jog_rate(jrate):
  epics.caput(ax+'.JVEL', jrate)

# set the velocity
def set_speed(velo):
  epics.caput(ax+'.VELO', velo)

# disable pause mode
def no_pause():
  epics.caput(ax+'.SPMG', 3)

# returns true if the motor is in motion
def moving():
  #done_moving_flag = epics.caget(ax+'.DMOV') == 1
  #movement_in_progress_flag = epics.caget(ax+'.MIP') == 1
  #return (not done_moving_flag) or (movement_in_progress_flag)
  return (not (epics.caget(ax+'.DMOV') == 1))

def get_motor_status():
  stup = epics.caget(ax+'.STUP') # read status update field
  if stup != 0:
    logging.warning(f"Status update field = {stup}, can't request status update")
    return None
  epics.caput(ax+'.STUP',1)
  while(epics.caget(ax+'.STUP') != 0):
    pass
  return(int(epics.caget(ax+'.MSTA')))

def print_motor_status(verbose=True):
  motor_status = get_motor_status()
  if motor_status is not None:
    logging.info(f"Motor Status Bits: 0b{motor_status:>016b}")
  if (verbose == True):
    bitnames = [
      'DIRECTION',
      'DONE',
      'PLUS_LS',
      'HOME_LS',
      'unused',
      'SLIP_STALL',
      'HOME',
      'PRESENT',
      'PROBLEM',
      'MOVING',
      'GAIN_SUPPORT',
      'COMM_ERROR',
      'MINUS_LS',
      'HOMED']

    for i in range(15-1):
      bit_val = ((motor_status>>i)&1) == 1
      logging.info(f"{str(i+1)+'.':<3} {bitnames[i]:<12} --> {bit_val}")

initial_position = get_pos()
logging.info(f"Initial position: {initial_position} [mm]")
print_motor_status()
get_jog_rate()
get_speed()

# now for the speed test
speed_max = 128000
jset = speed_max/200000
jtime = 100
jdistance = jset/200/16/2.54*jtime
set_jog_rate(jset)
set_speed(1.5) # max is 1.5875 = 2000/200/16*2.54

v_name = 'ACCL'
logging.info(f"{v_name} variable: {epics.caget(ax+'.'+v_name)}")

v_name = 'ACCL'
v_val = 1.0
epics.caput(ax+'.'+v_name, v_val)
#logging.info(f"{v_name} variable: {epics.caget(ax+'.'+variable)}")

# jog fwd (fwd is down)
#jog(forward=False, duration=10)

#down is more positive
goto(-100)

# jog rev
#jog(forward=False, duration=5)


jget = get_jog_rate()
speed = get_speed()
#logging.info(f"Jogging at {jget} Hz for {jtime} seconds so we expect to have {jdistance} mm of displacement...")   
#jog(forward=True, duration=jtime)
                   
# goto an exact position
#goto(2.0)

#goto(0.0, block=False)
#time.sleep(0.2)
print_motor_status()

while moving(): pass
final_position = get_pos()
logging.info(f"Final position: {final_position} [mm]")
print_motor_status()

logging.debug("Done")
