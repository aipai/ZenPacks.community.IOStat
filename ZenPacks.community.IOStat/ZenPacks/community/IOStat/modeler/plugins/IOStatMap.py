###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2007, 2009 Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

__doc__ = """IOStatMap

IOStatMap maps the phisical device to objects

"""

import re

from Products.ZenUtils.Utils import unsigned
from Products.DataCollector.plugins.DataMaps import ObjectMap
from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetTableMap

class IOStatMap(SnmpPlugin):

    maptype = "IOStatMap"
    compname = "hw"
    relname = "iostates"
    modname = "ZenPacks.community.IOStat.IOStat"
    deviceProperties = SnmpPlugin.deviceProperties + (
      'zIOStatMapIgnoreNames', 'zIOStatMapIgnoreTypes')

    snmpGetTableMaps = (
        GetTableMap('smTable', '.1.3.6.1.4.1.8072.1.3.2.4.1.2', 
        {
         '.10.105.111.115.116.97.116.85.116.105.108':'util',
         '.17.105.111.115.116.97.116.68.101.118.105.99.101.68.101.115.99.114':'title',
         '.17.105.111.115.116.97.116.68.101.118.105.99.101.73.110.100.101.120':'snmpindex',
        }
        ),
    )


    def process(self, device, results, log):
        """Process SNMP information from this device"""
        log.info('Modeler %s processing data for device %s', self.name(), device.id)
        getdata, tabledata = results
        log.debug("%s tabledata = %s", device.id, tabledata)
        smtable = tabledata.get("smTable")
        if smtable is None:
            log.error("Unable to get data for %s from smTable"
                          " -- skipping model" % device.id)
            return None

        skipfsnames = getattr(device, 'zIOStatMapIgnoreNames', None)
        skipfstypes = getattr(device, 'zIOStatMapIgnoreTypes', None)
        maps = []
        rm = self.relMap()
        for sm in smtable.values():
            om = self.objectMap(sm)
            om.id = self.prepId(om.title)
            log.info("IOStatMap %s, %s", device.id, str(om))
            rm.append(om)
        maps.append(rm)
        return maps


