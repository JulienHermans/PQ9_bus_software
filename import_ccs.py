#!/usr/bin/env python#

import sys
import subprocess
from subprocess import call
import functions
#import pip

#path = sys.argv[1:]
path = "/Users/nchronas/Documents/repos/delfiPQ/workspace7/"

print "Workspace dir:", path

print "Cloning repos"

software = ["git clone https://github.com/nchronas/ADB_software.git",
  	"git clone https://github.com/nchronas/EPS_software.git",
	"git clone https://github.com/nchronas/OBC_software.git",
	"git clone https://github.com/nchronas/ADCS_software.git",
	"git clone https://github.com/nchronas/RED_software.git",
	"git clone https://github.com/nchronas/COMMS_software.git",
	"git clone https://github.com/nchronas/PQ9_bus_software.git",
	"git clone https://github.com/nchronas/INA226.git",
	"git clone https://github.com/nchronas/TMP100.git",
	"git clone https://github.com/nchronas/MB85RS256A.git",
	"git clone https://github.com/nchronas/LTC2942.git"]

functions.function_clone()

print "Making RED project"

working_dir = path + "RED_software"

pq9_path = path + "PQ9_bus_software/"

print "Creating folders"

call(["mkdir", "ttc"], cwd=working_dir)

print "Creating symlinks"

folder = "RED_software/"

functions.function_pq9("delfiPQ/RED/HAL/RED_Board.h")
functions.function_pq9("delfiPQ/RED/HAL/RED_Board.c")


folder = "RED_software/ttc/"

software_RED = ["delfiPQ/HAL/hal_functions.c",
	"delfiPQ/RED/HAL/hal_subsystem.c",
	"delfiPQ/RED/devices.c",
	"delfiPQ/RED/fm.c",
	"delfiPQ/RED/housekeeping.c",
	"delfiPQ/RED/parameters.c",
	"delfiPQ/RED/subsystem_pool.c",
	"delfiPQ/RED/subsystem.c"]

software_PQ = ["delfiPQ/OSAL/osal.c",
	"delfiPQ/packet_engine.c",
	"delfiPQ/satellite.c",
	"delfiPQ/PQ9_bus_engine.c"]

software_core = ["core/function_management_service.c",
	"core/housekeeping_service.c",
	"core/packet_stats.c",
	"core/packet_utilities.c",
	"core/ping_service.c",
	"core/pkt_pool.c",
	"core/verification_service.c",
	"core/queue.c"]

functions.function_RED()	

print "Input to ccs directories"
print pq9_path + "delfiPQ/RED"
print pq9_path + "delfiPQ/RED/HAL"
print pq9_path + "delfiPQ/HAL"
print pq9_path + "delfiPQ/OSAL"
print pq9_path + "delfiPQ"
print pq9_path + "core"
print pq9_path + "services"

print "Making ADB project"

working_dir = path + "ADB_software"

pq9_path = path + "PQ9_bus_software/"

print "Creating folders"

call(["mkdir", "libs"], cwd=working_dir)
call(["mkdir", "ttc"], cwd=working_dir)

print "Creating symlinks"

folder = "ADB_software/"

functions.function_pq9("delfiPQ/ADB/HAL/ADB_Board.h")
functions.function_pq9("delfiPQ/ADB/HAL/ADB_Board.c")

folder = "ADB_software/ttc/"

software_ADB = ["delfiPQ/HAL/hal_functions.c",
	"delfiPQ/ADB/HAL/hal_subsystem.c",
	"delfiPQ/ADB/devices.c",
	"delfiPQ/ADB/housekeeping.c",
	"delfiPQ/ADB/parameters.c",
	"delfiPQ/ADB/subsystem_pool.c",
	"delfiPQ/ADB/subsystem.c"]
	
software_core.append("core/testing.c")

functions.function_ADB()

folder = "ADB_software/libs/"

functions.function_path("TMP100/TMP100.c")
functions.function_path("INA226/INA226.c")


print "Input to ccs directories"
print pq9_path + "delfiPQ/ADB"
print pq9_path + "delfiPQ/ADB/HAL"
print pq9_path + "delfiPQ/HAL"
print pq9_path + "delfiPQ/OSAL"
print pq9_path + "delfiPQ"
print pq9_path + "core"
print path + "INA226"
print path + "TMP100"

print "Making EPS project"

working_dir = path + "EPS_software"

pq9_path = path + "PQ9_bus_software/"

print "Creating folders"

call(["mkdir", "libs"], cwd=working_dir)
call(["mkdir", "ttc"], cwd=working_dir)

print "Creating symlinks"

folder = "EPS_software/"

functions.function_pq9("delfiPQ/EPS/HAL/EPS_Board.h")
functions.function_pq9("delfiPQ/EPS/HAL/EPS_Board.c")


folder = "EPS_software/ttc/"

software_EPS = ["delfiPQ/HAL/hal_functions.c",
	"delfiPQ/EPS/HAL/hal_subsystem.c",
	"delfiPQ/EPS/devices.c",
	"delfiPQ/EPS/fm.c",
	"delfiPQ/EPS/housekeeping.c",
	"delfiPQ/EPS/parameters.c",
	"delfiPQ/EPS/safety_check.c",
	"delfiPQ/EPS/subsystem_pool.c",
	"delfiPQ/EPS/subsystem.c"]

functions.function_EPS()

folder = "EPS_software/libs/"

functions.function_path("TMP100/TMP100.c")
functions.function_path("INA226/INA226.c")
functions.function_path("LTC2942/LTC2942.c")
functions.function_path("MB85RS256A/MB85RS256A.c")


print "Input to ccs directories"
print pq9_path + "delfiPQ/EPS"
print pq9_path + "delfiPQ/EPS/HAL"
print pq9_path + "delfiPQ/HAL"
print pq9_path + "delfiPQ/OSAL"
print pq9_path + "delfiPQ"
print pq9_path + "core"
print path + "INA226"
print path + "TMP100"
print path + "MB85RS256A"
print path + "LTC2942"

print "Making OBC project"

working_dir = path + "OBC_software"

pq9_path = path + "PQ9_bus_software/"

print "Creating folders"

call(["mkdir", "libs"], cwd=working_dir)
call(["mkdir", "ttc"], cwd=working_dir)

print "Creating symlinks"

folder = "OBC_software/"

functions.function_pq9("delfiPQ/OBC/HAL/OBC_Board.h")
functions.function_pq9("delfiPQ/OBC/HAL/OBC_Board.c")


folder = "OBC_software/ttc/"

software_OBC = ["delfiPQ/HAL/hal_functions.c",
	"delfiPQ/OBC/HAL/hal_subsystem.c",
	"delfiPQ/OBC/devices.c",
	"delfiPQ/OBC/fm.c",
	"delfiPQ/OBC/housekeeping.c",
	"delfiPQ/OBC/parameters.c",
	"delfiPQ/OBC/rf_packet.c",
	"delfiPQ/OBC/subsystem_pool.c",
	"delfiPQ/OBC/subsystem.c"]

software_core.insert(0, "core/en_data_service.c")

functions.function_OBC()

folder = "OBC_software/libs/"

functions.function_path("TMP100/TMP100.c")
functions.function_path("INA226/INA226.c")
functions.function_path("MB85RS256A/MB85RS256A.c")


print "Input to ccs directories"
print pq9_path + "delfiPQ/OBC"
print pq9_path + "delfiPQ/OBC/HAL"
print pq9_path + "delfiPQ/HAL"
print pq9_path + "delfiPQ/OSAL"
print pq9_path + "delfiPQ"
print pq9_path + "core"
print path + "INA226"
print path + "TMP100"
print path + "MB85RS256A"

print "Making ADCS project"

working_dir = path + "ADCS_software"

pq9_path = path + "PQ9_bus_software/"

print "Creating folders"

call(["mkdir", "libs"], cwd=working_dir)
call(["mkdir", "ttc"], cwd=working_dir)

print "Creating symlinks"

folder = "ADCS_software/"

functions.function_pq9("delfiPQ/ADCS/HAL/ADCS_Board.h")
functions.function_pq9("delfiPQ/ADCS/HAL/ADCS_Board.c")


folder = "ADCS_software/ttc/"

software_ADCS = ["delfiPQ/HAL/hal_functions.c",
	"delfiPQ/ADCS/HAL/hal_subsystem.c",
	"delfiPQ/ADCS/devices.c",
	"delfiPQ/ADCS/fm.c",
	"delfiPQ/ADCS/housekeeping.c",
	"delfiPQ/ADCS/parameters.c",
	"delfiPQ/ADCS/subsystem_pool.c",
	"delfiPQ/ADCS/subsystem.c"]

software_core.remove("core/en_data_service.c")

functions.function_ADCS()

folder = "ADCS_software/libs/"

functions.function_path("TMP100/TMP100.c")
functions.function_path("INA226/INA226.c")
functions.function_path("MB85RS256A/MB85RS256A.c")


print "Input to ccs directories"
print pq9_path + "delfiPQ/ADCS"
print pq9_path + "delfiPQ/ADCS/HAL"
print pq9_path + "delfiPQ/HAL"
print pq9_path + "delfiPQ/OSAL"
print pq9_path + "delfiPQ"
print pq9_path + "core"
print path + "INA226"
print path + "TMP100"
print path + "MB85RS256A"

print "Making COMMS project"

working_dir = path + "COMMS_software"

pq9_path = path + "PQ9_bus_software/"

print "Creating folders"

call(["mkdir", "libs"], cwd=working_dir)
call(["mkdir", "ttc"], cwd=working_dir)

print "Creating symlinks"

folder = "COMMS_software/"

functions.function_pq9("delfiPQ/COMMS/HAL/COMMS_Board.h")
functions.function_pq9("delfiPQ/COMMS/HAL/COMMS_Board.c")


folder = "COMMS_software/ttc/"

software_COMMS = ["delfiPQ/HAL/hal_functions.c",
	"delfiPQ/COMMS/HAL/hal_subsystem.c",
	"delfiPQ/COMMS/devices.c",
	"delfiPQ/COMMS/fm.c",
	"delfiPQ/COMMS/housekeeping.c",
	"delfiPQ/COMMS/parameters.c",
	"delfiPQ/COMMS/rf_packet.c",
	"delfiPQ/COMMS/subsystem_pool.c",
	"delfiPQ/COMMS/subsystem.c"]

software_core.insert(0, "core/en_data_service.c")

functions.function_COMMS()

folder = "COMMS_software/libs/"

functions.function_path("TMP100/TMP100.c")


print "Input to ccs directories"
print pq9_path + "delfiPQ/COMMS"
print pq9_path + "delfiPQ/COMMS/HAL"
print pq9_path + "delfiPQ/HAL"
print pq9_path + "delfiPQ/OSAL"
print pq9_path + "delfiPQ"
print pq9_path + "core"
print path + "TMP100"


print "Install pyserial, you need to have pip"
print """pip.main(['install', "pyserial"])"""

print "Dont forget to:"
print "add the ti-rtos kernel (import from simplelink and add build dependency)"
print "Add c99 flag"
print "Modify simplelink uart driverlib for pq9 packet handling"
