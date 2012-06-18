#!/usr/bin/python

from sqlobject import *
import sys, os
import datetime

conn_str = 'postgres://postgres:I\ am\ a\ child\ of\ God@localhost/postgres'
conn = connectionForURI(conn_str)
sqlhub.processConnection = conn


debug = 0

class Host(SQLObject):
    ip = StringCol(length = 15)
    state = StringCol(length = 25, default = None)
    reason = StringCol(length = 25, default = None)
    hostname = StringCol(length = 100, default = None)
    os_type = StringCol(length = 100, default = None)
    os_vendor = StringCol(length = 100, default = None)
    os_family = StringCol(length = 100, default = None)
    os_gen = StringCol(length = 100, default = None)
    osclass_accuracy = IntCol(default = None)
    uptime = IntCol(default = None)
    lastboot = StringCol(default = None)
    finished = StringCol(default = None)
    elapsed = StringCol(default = None)
    osmatch_name = StringCol(length = 50, default = None)
    osmatch_accuracy = StringCol(length = 25, default = None)
    date_modified = DateTimeCol(default = datetime.datetime.now())

## Service class
class Service(SQLObject):
    service = StringCol(length = 15)
    default_port = IntCol()
    date_modified = DateTimeCol(default = datetime.datetime.now())

    def add_service(service, default_port):
        if debug > 0:
            Service._connection.debug = True
        service = Service(service = service, default_port = default_port, date_modified = datetime.datetime.now())
        return service

    def select_service(service):
        if debug > 0:
            Service._connection.debug = True
        service = Service.select(Service.q.service == service)
        return service

    def delete_service(service_name):
        if debug > 0:
            Service._connection.debug = True
        Service.delete(Service.select(Service.q.service == service_name).getOne().id)

## Host Service class
class Host_service(SQLObject):
    ip = StringCol(length = 20)
    port_id = IntCol()
    protocol = StringCol(length = 25)
    state = StringCol(length = 15, default = None)
    reason = StringCol(length = 50, default = None)
    reason_ttl = IntCol(default = None)
    service_name = StringCol(length = 100, default = None)
    product = StringCol(length = 50, default = None)
    version = StringCol(length = 50, default = None)
    extrainfo = StringCol(length = 50, default = None)
    ostype = StringCol(length = 50, default = None)
    method = StringCol(length = 50, default = None)
    conf = IntCol(default = None)
    date_modified = DateTimeCol(default = datetime.datetime.now())

## Service script
class Service_script(SQLObject):
    ip = StringCol(length = 20)
    port_id = IntCol()
    protocol = StringCol(length = 25)
    service_name = StringCol(length = 50)
    script_id = StringCol(length = 50)
    script_output = StringCol()
    date_modified = DateTimeCol(default = datetime.datetime.now())

class Os_signature(SQLObject):
    os_signature = StringCol()
    os_signature_source = StringCol()
    os_vendor = StringCol(length = 50)
    os_name = StringCol(length = 50)
    os_version = StringCol(length = 25)
    os_release = StringCol(length = 25)
    date_modified = DateTimeCol(default = datetime.datetime.now())
#def test(ip, port_id, protocol, state, service_name, service_desc, reason, osclass, osmatch, lastboot):
    ## test of host methods

    #host = add_host(ip, osclass, osmatch, lastboot)
    #print list(select_host(ip))
    #delete_host(ip)
    #print list(select_host(ip))
    
    
    ## test of service methods

    #serviceid = add_service(service_name, port_id)
    #print list(select_service(service_name))
    #delete_service(service_name)
    #print list(select_service(service_name))

    ## test of host service methods

    #host_service_id = add_host_service(ip, port_id, protocol, state, service_name, service_desc, reason)
    #print host_service_id
    #print list(select_host_service(ip, port_id))
    #delete_host_service(ip, port_id)
    #print list(select_host_service(ip, port_id))

#test("205.118.116.101", int(22), "tcp", "open", "ssh", "", "", "Linux Linux 2.6.X general purpose", "", "Wed May 30 08:21:41 2012")
#test("205.118.116.101", int(22), "tcp", "open", "ssh", "", "")
