import libvirt
from xml.etree import ElementTree as ET

class LibvirtDomain(object):
    def __init__(self, src):
        if src == None:
            libvirturi = "qemu:///system"
        else:
            libvirturi = src
        self.conn = libvirt.open(libvirturi)

    def lookup(self, token):
        dom = self.conn.lookupByUUIDString(token)
        xml = dom.XMLDesc(0)
        root = ET.fromstring(xml)
        graphicselem = root.find("devices/graphics")
        port = graphicselem.get("port")
        return ("localhost", port)