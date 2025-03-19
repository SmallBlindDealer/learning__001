
LB(HA Proxy or Zuul), types of LB, LB Algo(Consistent Hashing)
difference in L4 and L7 LB
Message Broker
APIgetway
Forwad and reverse Proxy
CDN
Event Driven Design
Event Sourcing
Service Discovery(Kong, Netflix Eureka)
Gossip Protocol
Health check in APIGetway, LB, ServiceDiscovery
ACID vs CAP
CQS and CQRS
CRAQ

Consesnses Algo in Distributed System
        --RAFT
        --POXOS
        --leader based
        --voting based

Distributed Txn
    Sync---> 2 or 3 phase commit
    Async--> Saga Orchestation vs Coriography

RESTAPI best Practice

TCP/HTTP
TLS/SSL
Layer 4 and Layer 7
websocket
sort polling
long polling
http streaming
TCP
UDP

Types of cloud
    --public
    --private
    --hybrid

Distributed System(Zookeepers)
Distributed Kernel(Apache Mesos---->Apache Marathon)

LLD:
    Creational:
        ...
    Structural:
        ...
    Behavioral:
        ...

Scalability
Performance
Fault Tolerance
Availability
Consistency
Partition Tolerance
Durability


tech stack:
monitoring: (Prometheus--->Grafana), NewRelic
logging: ELK
other:--> Kafka, Redis, MongoDB(document store), Cassandra(Key value store (good for high read and write traffic))

How DB works
benefit of gRPC and Protobuffer
Handling failures and retrying messages or events
Difference in multithreading, multiprocessing and Async
ETL pipline creation
Bloom filter
AutoScaling, AutoHealing



working on Big Data
Data Egineering:
    DVC(data version control)
    Hbash (hadoop db)
    HDFS(storage)
    MapReduce(compute on CPU)
    Query_on_HDFS_file_data
        Hive(SQL)
        Pig(NoSQL)
    Spark(compute on RAM,  batch processing)
    Flink(compute on RAM, real time processing)
    DataBrick(run on Spark cluster)
    SnowFlake(run on Spark cluster)
    Airflow(Oozie)


 --------------------------------------------------------------------
 load shedding vs cuircuit breaker vs rate limiting
 zookeepers--distributed coordination service
    consensus protocol
    strong consistency
    fault tolerant
    efficient metadata management
    leader election



365*24*60*60=31536000--> 32*10^6
99.00%       -->315360---------5
99.90%       -->31536----------4
99.99%       -->3153.6---------3
99.999%      -->315.36---------2
99.9999%     -->31.536---------1
99.99999%    -->3.1536---------0
99.999999%   -->3.1536*10^-1---(-1)
99.9999999%  -->3.1536*10^-2---(-2)

stateful vs stateless
nginx
single point of failure
retry/failover
socket sharding
purge request
    Content Delivery Networks (CDNs)
    Data Retention Management (DRTM)
    Software Systems
    Service Management Systems


Ulimit vs Gunicorn (Relationship and Key Difference)
concurrency vs consistency
bitmap index
redis pub sub
