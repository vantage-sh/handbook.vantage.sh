title: EFS Pricing | Cloud Cost Handbook

[Amazon EFS Pricing Page](https://aws.amazon.com/efs/pricing/){ .md-button target="_blank"}

## Summary

Amazon Elastic File System (EFS) is a scalable elastic file storage system, where workloads are scaled up and down automatically as files are added and removed. Some use cases include containerized and serverless applications, big data analytics, development and testing, database backups, and machine learning training.

## Pricing Dimensions

| Dimension | Description |
|--------|--------|
|Storage Classes|See the [Storage Classes](#storage-classes) section for more information.|
|File Systems|There are two file systems to choose from—EFS Regional File System (Multi-AZ) and EFS One Zone. With the Regional File System option, files are stored across at least three Availability Zones (AZ). For files where availability and durability are less important, One Zone stores files in just one AZ within an AWS region, at a much lower storage price.|
|Throughput Modes|There are two throughput modes—Elastic Throughput mode and Provisioned Throughput mode. Elastic Throughput mode is recommended for unpredictable peak throughput needs or spiky throughput usage. Use Provisioned Throughput for high peak throughput capacity. Elastic Throughput mode charges for reads and writes per GB transferred whereas Provisioned Throughput charges are based on MB/s. Also, Infrequent Access storage is more expensive using Provisioned Throughput.|
|Storage|Charges for storage vary depending on your region, as wall as your choice of storage class, file system, and throughput mode.|
|Data Transfer|With Elastic Throughput mode, you are charged for reads and writes per GB transferred. You are also charged for tiering between storage classes. Charges for writes are more expensive in the cost-optimized storage classes.|

## Storage Classes

Amazon EFS offers three storage classes, each with different pricing rates and functionality. Availability and cost are the tradeoffs, the more available the data is, the higher the storage costs are. Each EFS storage class is described below:

| Storage Class | Description |
|------|-----|
|EFS Standard|Standard is the high-speed, low-latency option for regularly accessed or modified data workloads.|
|EFS Infrequent Access|Providing the same features, durability, throughput, and IOPS scalability as Standard, the Infrequent Access class is ideal for workloads where the “sub-millisecond latencies” of Standard are not needed. Use this class for data that is accessed a few times a quarter.|
|EFS Archive|Just like Infrequent Access, Archive provides the same features, durability, throughput, and IOPS scalability as Standard. Archive is recommended for workloads where data is accessed a few times a year.|

Make use of EFS Lifecycle Management to set lifecycle policies to transition files into lower-cost storage classes after periods of no use.

<br/>

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Feb 5, 2024_
