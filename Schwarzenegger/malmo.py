from __future__ import print_function

from builtins import range
import MalmoPython
import os
import sys
import time

if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools
    print = functools.partial(print, flush=True)

# More interesting generator string: "3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"

missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
              <About>
                <Summary>gitlab.com/whoisZORZ</Summary>
              </About>
              
              <ServerSection>
                <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1"/>
				  <DrawingDecorator>
						<DrawSphere x="-27" y="70" z="0" radius="30" type="air"/>
				  </DrawingDecorator>
                  <ServerQuitFromTimeUp timeLimitMs="360000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Survival">
                <Name>ZORZBot</Name>
                <AgentStart/>
                <AgentHandlers>
                  <ObservationFromFullStats/>
                  <ContinuousMovementCommands turnSpeedDegs="180"/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

# Create default Malmo objects:

agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print('ERROR:',e)
    print(agent_host.getUsage())
    exit(1)
if agent_host.receivedArgument("help"):
    print(agent_host.getUsage())
    exit(0)

my_mission = MalmoPython.MissionSpec(missionXML, True)
my_mission_record = MalmoPython.MissionRecordSpec()

# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print("Error starting mission:",e)
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print("Waiting for the mission to start ", end=' ')
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)
agent_host.sendCommand("move 1")
print()
print("Mission running ", end=' ')



stevex = 0
stevez = 0
stevey = 0
steveyaw = 0
stevepitch = 0
elotteidx = 0
elotteidxj = 0
elotteidxb = 0
akadaly = 0

# Loop until mission ends:
while world_state.is_mission_running:
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)
		
if world state.number of observations since last state > 0:
	msg = world_state.observations[-1].text
	observations = json.loads(msg)
	nbr = observations.get("nbr3x3", 0)
	print("Mit latok: ", nbr)
	
	if "Yaw" in observations:
		steveyaw = observations["Yaw"]
	if "Pitch" in observations:
		stevepitch = observations["Pitch"]
	if "XPos" in observations:
		stevex = observations["XPos"]
	if "ZPos" in observations:
		stevez = observations["ZPos"]
	if "YPos" in observations:
		stevey = observations["YPos"]
		
	print ("Pozicio koordinatak: ", stevex, stevez, stevey)
	print ("Irany: ", steveyaw)
	print ("Nezet: ", stevepitch)
	
	if steveyaw >= 180-22.5 and steveyaw <= 180+22.5 :
		elotteidx = 1
		elotteidxj = 2
		elotteidxb = 0
		
	if steveyaw >= 180+22.5 and steveyaw <= 270-22.5 :
		elotteidx = 2
		elotteidxj = 5 
		elotteidxb = 1
		
	if steveyaw >= 270-22.5 and steveyaw <= 270+22.5 :
		elotteidx = 5
		elotteidxj = 8
		elotteidxb = 2
		
	if steveyaw >= 270+22.5 and steveyaw <= 360-22.5 :
		elotteidx = 8
		elotteidxj = 7
		elotteidxb = 5
		
	if steveyaw >= 360-22.5 or steveyaw  <= 0+22.5 :
		elotteidx = 7
		elotteidxj = 6 
		elotteidxb = 8
		
	if steveyaw >= 0+22.5 and steveyaw <= 90-22.5 :
		elotteidx = 6
		elotteidxj = 3
		elotteidxb = 7
		
	if steveyaw >= 90-22.5 and steveyaw <= 90+22.5 :
		elotteidx = 3
		elotteidxj = 0
		elotteidxb = 6
		
	if steveyaw >= 90+22.5 and steveyaw <= 180-22.5 :
		elotteidx = 0
		elotteidxj = 1
		elotteidxb = 3
		
	print ("racsindex", elotteidx)
	
	if nbr[elotteidx+9]!="air" or nbr[elotteidxj+9]!="air" or nbr[elotteidxb+9]!="air":
		print ("Nincs szabad utam, elottem: ", nbr[elotteidx+9])
		agent_host.sendCommand ("turn" + str(turn))
		akadaly = akadaly + 1
	else:
		print ("Szabad az ut!")
		agent_host.sendCommand ("turn 0")
		agent_host.sendCommand ("jump 0")
		agent_host.sendCommand ("attack 0")
		akadaly = 0
		
	if akadaly > 8:
		agent_host.sendCommand ("jump 1")
	
	lepes = lepes + 1
	if lepes > 100:
	lepes = 0
	if tav < 20:
		prevstevex = stevex
		prevstevez = stevez
		prevstevey = stevey
		turn = turn * -1
		agent_host.sendCommand ("attack 1")
	
	time.sleep(1)

print()
print("Mission ended")
# Mission has ended.
