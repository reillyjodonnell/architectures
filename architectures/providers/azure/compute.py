
from architectures.providers import _Azure

class _Compute(_Azure):
    _service_type = "compute"
    _icon_dir = "icons/azure/compute"


class AvailabilitySets(_Compute):
    _icon = "availability-sets.png"


class BatchAccounts(_Compute):
    _icon = "batch-accounts.png"


class CitrixVirtualDesktopsEssentials(_Compute):
    _icon = "citrix-virtual-desktops-essentials.png"


class CloudServicesClassic(_Compute):
    _icon = "cloud-services-classic.png"


class CloudServices(_Compute):
    _icon = "cloud-services.png"


class CloudsimpleVirtualMachines(_Compute):
    _icon = "cloudsimple-virtual-machines.png"


class ContainerInstances(_Compute):
    _icon = "container-instances.png"


class ContainerRegistries(_Compute):
    _icon = "container-registries.png"


class DiskSnapshots(_Compute):
    _icon = "disk-snapshots.png"


class Disks(_Compute):
    _icon = "disks.png"


class FunctionApps(_Compute):
    _icon = "function-apps.png"


class KubernetesServices(_Compute):
    _icon = "kubernetes-services.png"


class MeshApplications(_Compute):
    _icon = "mesh-applications.png"


class SAPHANAOnAzure(_Compute):
    _icon = "sap-hana-on-azure.png"


class ServiceFabricClusters(_Compute):
    _icon = "service-fabric-clusters.png"


class VirtualMachineClassic(_Compute):
    _icon = "virtual-machine-classic.png"


class VirtualMachineImages(_Compute):
    _icon = "virtual-machine-images.png"


class VirtualMachineLinux(_Compute):
    _icon = "virtual-machine-linux.png"


class VirtualMachineWindows(_Compute):
    _icon = "virtual-machine-windows.png"


class VirtualMachine(_Compute):
    _icon = "virtual-machine.png"


# Aliases

ACR = ContainerRegistries
AKS = KubernetesServices
