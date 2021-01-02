
from architectures.providers import _Azure


class _Storage(_Azure):
    _service_type = "storage"
    _icon_dir = "icons/azure/storage"


class ArchiveStorage(_Storage):
    _icon = "archive-storage.png"


class Azurefxtedgefiler(_Storage):
    _icon = "azurefxtedgefiler.png"


class BlobStorage(_Storage):
    _icon = "blob-storage.png"


class DataBoxEdgeDataBoxGateway(_Storage):
    _icon = "data-box-edge---data-box-gateway.png"


class DataBox(_Storage):
    _icon = "data-box.png"


class DataLakeStorage(_Storage):
    _icon = "data-lake-storage.png"


class GeneralStorage(_Storage):
    _icon = "general-storage.png"


class NetappFiles(_Storage):
    _icon = "netapp-files.png"


class QueuesStorage(_Storage):
    _icon = "queues-storage.png"


class StorageAccountsClassic(_Storage):
    _icon = "storage-accounts-classic.png"


class StorageAccounts(_Storage):
    _icon = "storage-accounts.png"


class StorageExplorer(_Storage):
    _icon = "storage-explorer.png"


class StorageSyncServices(_Storage):
    _icon = "storage-sync-services.png"


class StorsimpleDataManagers(_Storage):
    _icon = "storsimple-data-managers.png"


class StorsimpleDeviceManagers(_Storage):
    _icon = "storsimple-device-managers.png"


class TableStorage(_Storage):
    _icon = "table-storage.png"


# Aliases
