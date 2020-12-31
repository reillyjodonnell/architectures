from . import _Azure

class _AI(_Azure):
    _type = "compute"
    _icon_dir = "icons/azure/compute"

class VirtualMachine(_AI):
    _icon = "virtual-machine.png"