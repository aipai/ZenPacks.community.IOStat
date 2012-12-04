from Globals import InitializeClass
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.HWComponent import *
from Products.ZenModel.ZenossSecurity import *
from cmath import *

SEV_CLEAN    = 0
SEV_DEBUG    = 1
SEV_INFO     = 2
SEV_WARNING  = 3
SEV_ERROR    = 4
SEV_CRITICAL = 5

import logging
log = logging.getLogger("zen.iostat.IOStat")

def manage_addIOStat(context, id, title = None, REQUEST = None):
    """make a filesystem"""
    hd = IOStat(id, title)
    context._setObject(id, hd)
    hd = context._getOb(id)
    hd.index_object()

    if REQUEST is not None:
        REQUEST['RESPONSE'].redirect(context.absolute_url()
                                     +'/manage_main') 

#addIOStat = DTMLFile('dtml/addIOStat',globals())

class IOStat(HWComponent):
    util = 0
    portal_type = meta_type = 'IOStat'
    
    _properties = HWComponent._properties + (
        {'id':'title', 'type':'string', 'mode':'w'},
        {'id':'util', 'type':'int', 'mode':'w'},
    )
    
    _relations = HWComponent._relations + (
        ("hw", ToOne(ToManyCont, "Products.ZenModel.DeviceHW", "iostates")),
        )
    
    factory_type_information = (
        {
            'id'                : 'IOStat',
            'meta_type'         : 'IOStat',
            'description'       : """IOStates""",
            'icon'              : 'HardDisk_icon.gif',
            'product'           : 'IOStat',
            'factory'           : 'manage_addIOStatIOStat',
            'immediate_view'    : 'viewIOStatIOStat',
            'actions'           :
            (
                { 'id'          : 'status',
                  'name'        : 'Status',
                  'action'      : 'viewIOStatIOStat',
                  'permissions' : (ZEN_VIEW, )
                },
            )
        },
    )

    def getRRDNames(self):
        """ 
        Return the datapoint name of this filesystem 'usedBlocks_usedBlocks'
        """
        return ['util_util']
        
    def viewName(self):
        """
        Return the mount point name of a filesystem '/boot'
        """
        return self.title
    name = viewName
    
InitializeClass(IOStat)
