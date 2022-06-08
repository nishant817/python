# SYSTEM DESIGN 

## Features of distributed system
   * Scalability
   * Reliability
      * Data is not lost ever
      * Increase redundancy. Have copies of DB
      * Remove single point of failure
   * Availability
      * Have copies of everything (LB, webserver)
   * Efficiency: Measured by
      * Latency (response time)
      * Throughput (bandwidth) - number of items delivered per unit time
   * Maintainability or serviceability


## Databases
   * Scale Horizontally: Cassandra, MongoDB
   * Scale Vertically: Relational
   * Relational
   * Non-Relational
      * Key-Value Store
         * Very fast as most data is in-momory
         * usage: Caching, configs, request/response, etc.
         * e.g. Redis, MemCache, DynamoDB
      * Column Based
         * Mid way of RDBMS and Document DB
      * Document Based
         * When schema not clearly defined
         * When not sure how schema will evolve
         * Support heavy read/write
         * Highly scalable
         * Sharding
         * Dynamic data
         * Special query operation/aggregation
      * Search DB

### Database Selection
   * Factors
      1. Structure of Data
      2. Query Pattern
      3. Amount of Scale
      4. CAP Theorem based
         1. Consistency + Availability. No PT
            * Mostly Relational using primary-secondary or master-slave architecture
            * Oracle, MySQL, MSSQL, Postgrace
         2. Consistency + Partition Tolerance. No Availability
            * Availability (write operation) is sacrificed to maintain consistency and PT
            * MongoDB
            * Redis
            * Couchbase
            * Apache HBase
            * Memcache
         3. Availability + Partition Tolerance. No Consistency
            * Read/write both allowed when partition happens. i.e. consistency sacrificed
            * Casandra
            * Amazon Dynamo DB
            * CouchBase
      5. PACELC: If partition then 'choose Availability or Consistency' Else 'choose Latency or Consistency'
          
   * Caching
      * Redis
      * Memchached
      * etcd
      * HazelCast
      * Usually Key-Value Pairs
   * File Storage (Blob Storage)
      * Amazon S3
      * +CDN -> to disctribute the content in different geographical location
   * Lots of Data, Lots of Attributes, Varieties of Queries -> Use Document DB
      * MongoDB
      * CouchBase
   * Ever Increasing Data e.g. Uber, Finite Queries -> Columnar DB
      * Casandra
      * HBase
   * Text Search capability/Fuzzy Search
      * Elastic Search
      * Solr
      * e.g. e-commerve services, netflix
      * Uses Text Search Engine
      * note: In both cases, availability and redundancy is good. But data can be lost. Should not be used as permanent storage
   * Metrics Data
      * InfluxDB
      * Open TSDB
      * Time series database
      * e.g. Grafana, Graphite, Prometheous
      * No random updates
      * Only sequential update in append-only mode
      * Read queries are bulk read queries based on time range
   * Analytics
      * Hadoop
      * Data Warehouse
      * Used for offline reporting

## System Design Steps
   * Functional Requirements
   * Non-Functional Requirements
   * Design Consideration
      * Read Heavy or write heavy?
      * Read/Write ratio
      * Min, Max, Avg size of API call
      * Number of new posts per unit time
   * Capacity estimation
      * Database size
      * Network bandwidth / traffic estimate 