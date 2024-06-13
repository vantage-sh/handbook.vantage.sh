title: DynamoDB Pricing | Cloud Cost Handbook

[Amazon DynamoDB Pricing Page](https://aws.amazon.com/dynamodb/pricing/){ .md-button target="_blank"}

## Summary

DynamoDB is Amazon's primary managed NoSQL database service.

It offers single-digit millisecond latency, scales to effectively unlimited requests per second, and has (largely) predictable pricing.

DynamoDB, like most NoSQL datastores, differs substantially from relational databases—it can only be queried via primary key attributes on the base table and indexes.

## Pricing Dimensions

| Dimension      | Options                                                     | Description                                                                                                                                                 |
|----------------|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Billing Mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html#HowItWorks.OnDemand)   | `On Demand, Provisioned Throughput`                         | Choose between paying per read/write or per allocated requests per second throughput.                                                                        |
| [Write Type](https://aws.amazon.com/blogs/aws/new-amazon-dynamodb-transactions/)     | `Standard, Transactional`                                   | Transactional operations allow *ACID guarantees* at twice the standard cost.                                                                                 | 
| [Read Type](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html)        | `Eventually Consistent, Strongly Consistent, Transactional` | Dynamo reads are by default *Eventually Consistent* - when you read from a table, the response might not reflect the results of a recently completed write. | 
| [Read Operation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html) | `GetItem, Scan, Query`                                      | Scans return the entire contents of a table; Queries allow a much faster & cheaper read of a subsection of the table.                                        | 
| [Indexes](https://www.dynamodbguide.com/secondary-indexes/)         | `None, Local Secondary Index, Global Secondary Index`       | Indexes allow an alternate set of `partition_key` + `sort_key` to be used for queries.                                                                       | 

## Billing Mode

"Use on-demand until it hurts" - [Alex DeBrie, quoting Jared Short](https://twitter.com/geoff_baskwill/status/1421181922097737729)

Provisioned Throughput is cheaper if you have a meaningful number of reads/writes *distributed evenly across time*. Any reads/writes above the provisioned threshold *will fail*, so it is not well suited to bursty or unpredictable workloads.

Provisioned Throughput includes optional Auto Scaling if throughput thresholds are being exceeded ([docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)).

[AWS Free Tier](https://aws.amazon.com/free) includes 25 reads/writes per second of Provisioned Throughput (across any number of tables) but *does not* include any on-demand mode usage.

| Billing Mode           | Unit                          | Unit Definition                                            |
|------------------------|-------------------------------|------------------------------------------------------------|
| On-Demand              | Read Request Unit (RRU)   | Read two <4KB items, eventually consistent                 |
| On-Demand              | Write Request Unit (WRU)  | Write one <1KB item                                        |
| Provisioned Throughput | Read Capacity Unit (RCU)  | Two reads *per second* (<4KB items), eventually consistent |
| Provisioned Throughput | Write Capacity Unit (WCU) | One write *per second* (<1KB item)                         |


## Write Type

Standard writes are relatively straightforward and include single-item writes (`table.put_item`) and batch writes (`batch.put_item`).

Transactions (`client.execute_transaction`) group up to 25 writes (or reads, updates, or deletes) together and *guarantee that they succeed or fail together.*

For a given write of an item up to *1KB* in size:

| Type                 | Cost                       |
|----------------------|----------------------------|
| Standard Single Item | 1 WRU                      |
| Standard Batch       | 1 WRU (per item)           |
| Transactional        | 2 WRU (2x)                 |
| Oversize 4KB Item    | 4 WRU (4x, size dependent) |


## Read Type

Part of what makes DynamoDB a compelling offering is its hybrid approach to the CAP theorem[^1]—it can adjust between eventually and strongly consistent as needed.

Wherever acceptable to the business needs and current data modeling, it is faster and cheaper to use eventually consistent reads.

That said, some business logic unequivocally dictates strongly consistent reads (e.g. an ATM reading a customer's balance).

For a given read of an item up to *4KB* in size:

| Type                  | Cost       |
|-----------------------|------------|
| Eventually Consistent | 0.5 RRU    |
| Strongly Consistent   | 1 RRU (2x) |
| Transactional         | 2 RRU (4x) |


## Read Operation


Getting a single item is as simple as providing its `partition_key` (and `sort_key` if the table has one).

Queries, however, are much more involved. NoSQL databases like DynamoDB can require significant upfront data modeling work to enable the query flexibility that SQL-based databases have by default.

Scans require reading the entire table and are correspondingly slow and expensive. Wherever possible, *avoid scanning Dynamo tables.*

| Type      | Cost                                 |
|-----------|--------------------------------------|
| `GetItem` | 1 RRU                                |
| `Query`   | {# of items meeting query logic} RRU |
| `Scan`    | {# of items in table} RRU            |


## Indexes

Every DynamoDB table has a `partition_key` (`pk`) and optional `sort_key` (`sk`) specified at the time of creation.

Indexes allow alternate partition and sort keys to be used to query items. They may be created at any time and are automatically maintained as new items are written.

Indexes can help control costs in two primary ways:

1. Queries on a new index return fewer unnecessary items (than the alternative/existing query) and thus cost less RRUs.

2. Each index optionally allows a subset of item attributes to be **projected** to that index. Projecting a subset can save on read costs if items are regularly >4KB, but the projected attribute names+values sum to <4KB.[^2]

| Type                             | Primary Key Attributes                       |
|----------------------------------|----------------------------------------------|
| Base table                       | Initial `pk` + optional `sk`                 |
| Local Secondary Index (LSI)      | Initial `pk` + *different* `sk`              |
| Global Secondary Index (GSI)     | *Different* `pk` + optional *different* `sk` |

!!! info
    The provisioned throughput settings of a global secondary index is separate from those of its base table.

## Other

DynamoDB tables can optionally enforce a **Time To Live (TTL)** on items in the table, such that they expire after that amount of time (guaranteed within +48 hours).

Dynamo exposes the time-ordered sequence of item-level changes on a given table via **DynamoDB Streams**. Reading change data from Streams is slightly cheaper per request than reading the table itself (on pay-per-use BillingMode). The first 2.5M reads per month are free.

## Further Reading

* An overview of the architecture of DynamoDB can be found in the [DynamoDB Paper](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
* You can, if you so choose, use a SQL-like syntax to interface with DynamoDB via [PartiSQL support](https://aws.amazon.com/about-aws/whats-new/2020/11/you-now-can-use-a-sql-compatible-query-language-to-query-insert-update-and-delete-table-data-in-amazon-dynamodb/)


<br/>


[^1]: The [CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem) is a computer science theorem that observes that a distributed datastore cannot guarantee all three of Consistency, Availability, and Partition Tolerance.

[^2]: If a query to an index with projection requests attribute values not in the projected values, it will incur twice the normal read cost, as the remaining attribute values must be fetched from the base table.

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Jul 31, 2021_
