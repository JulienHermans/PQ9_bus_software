#ifndef __SUBSYSTEM_H
#define __SUBSYSTEM_H

#include "satellite.h"
#include "packet_engine.h"
#include "satellite_ids.h"
//#include "packet_services.h"

#define SYSTEM_APP_ID _ADCS_APP_ID_

SAT_returnState route_pkt(pq9_pkt *pkt);

#endif