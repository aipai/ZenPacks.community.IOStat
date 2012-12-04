/*
###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
*/

(function(){

var ZC = Ext.ns('Zenoss.component');


ZC.IOStatPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'IOStat',
            autoExpandColumn: 'title',
            fields: [
                {name: 'uid'},
                {name: 'severity'},            
                {name: 'util'},
                {name: 'title'},
                {name: 'hasMonitor'},
                {name: 'monitor'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'title',
                dataIndex: 'title',
                header: _t('Name')
            },{
                id: 'util',
                dataIndex: 'util',
                header: _t('Util')
            }]
        });
        ZC.IOStatPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('IOStatPanel', ZC.IOStatPanel);
ZC.registerName('IOStat', _t('IOStat'), _t('IOStat'));
})();
