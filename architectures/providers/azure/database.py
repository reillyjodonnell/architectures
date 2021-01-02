
from architectures.providers import _Azure


class _Database(_Azure):
    _service_type = "database"
    _icon_dir = "icons/azure/database"


class BlobStorage(_Database):
    _icon = "blob-storage.png"


class CacheForRedis(_Database):
    _icon = "cache-for-redis.png"


class CosmosDb(_Database):
    _icon = "cosmos-db.png"


class DataLake(_Database):
    _icon = "data-lake.png"


class DatabaseForMariadbServers(_Database):
    _icon = "database-for-mariadb-servers.png"


class DatabaseForMysqlServers(_Database):
    _icon = "database-for-mysql-servers.png"


class DatabaseForPostgresqlServers(_Database):
    _icon = "database-for-postgresql-servers.png"


class ElasticDatabasePools(_Database):
    _icon = "elastic-database-pools.png"


class ElasticJobAgents(_Database):
    _icon = "elastic-job-agents.png"


class ManagedDatabases(_Database):
    _icon = "managed-databases.png"


class SQLDatabases(_Database):
    _icon = "sql-databases.png"


class SQLDatawarehouse(_Database):
    _icon = "sql-datawarehouse.png"


class SQLManagedInstances(_Database):
    _icon = "sql-managed-instances.png"


class SQLServerStretchDatabases(_Database):
    _icon = "sql-server-stretch-databases.png"


class SQLServers(_Database):
    _icon = "sql-servers.png"


class VirtualClusters(_Database):
    _icon = "virtual-clusters.png"


class VirtualDatacenter(_Database):
    _icon = "virtual-datacenter.png"


# Aliases
