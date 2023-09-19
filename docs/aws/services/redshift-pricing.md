title: Redshift Pricing | Cloud Cost Handbook

[Amazon Redshift Pricing Page](https://aws.amazon.com/redshift/pricing/){ .md-button target="_blank"}

## Summary
Redshift is a cloud data warehouse that enables organizations to analyze large volumes of data using SQL queries. The data can be structured and semi-structured across data warehouses, operational databases, and data lakes. With Redshift you can share and query live data across organizations, accounts, and regions.

## Pricing Dimensions
| Dimension  | Description |
| ------------- |-------------|
|[Node Type](https://instances.vantage.sh/redshift/){ target="_blank" }| You are billed an hourly rate based on your selected node type and node quantity for the duration your cluster is active. The recommended node types for Redshift are RA3 and DC2. Choose based on data size to ensure the best price and performance. If your data is under 1TB uncompress it is recommended to use DC2 Node. If your data is currently over 1TB uncompressed or will exceed 1TB in the future, it is recommended to use RA3.|
|[Paid Features](#paid-features)| Additional features can accrue additional costs.|
|Data Transfer|Data transfers between Redshift and S3 within the same AWS Region for tasks like backup, restore, load, and unload operations are free of charge. However, any other data transfers into and out of Redshift incur standard AWS data transfer rates.|
|Backup Storage|Redshift charges for manual snapshots you taken using the console, API, or CLI. This includes manual snapshots taken for RA3 clusters. Storing backups beyond the allocated storage capacity on DC and DS clusters results in additional charges based on the standard S3 storage rates. Should you retain recovery points beyond the initial free 24-hour period, they will lead to additional charges as part of RMS.|

## Paid Features

### Redshift Serverless
With Redshift Serverless you can run analytics and scale without setting up and managing warehouse infrastructure. It is ideal for difficult to predict compute needs, immediately needed ad-hoc analytics, and test and development environments. 

You only pay for the capacity used and capacity is automatically scaled up and down depending on need, as well as shutting off during inactivity. Data wearhouse capacity is measured in Redshift Processing Units (RPUs). You are billed in RPU-hours on a per-second basis. Since Redshift Serverless automatically provisions the appropriate resources, you do not need to choose a node type. The features concurrency scaling and Redshift Spectrum are included in the cost.

### Redshift Spectrum 
This feature enables you to execute SQL queries on data stored in [S3](/aws/services/s3-pricing). The billing is based on the volume of data scanned by Redshift Spectrum, which will be rounded up to the nearest megabyte, with a minimum fee of 10 MB per query.

### Redshift Managed Storage
Redshift Managed Storage is a feature that allows you to store and manage data within your Redshift cluster. It is exclusively available for RA3 node types. Billing is a fixed GB-month rate regardless of data size. Usage of managed storage is computed on an hourly basis, taking into account the total amount of data stored.

### Concurrency Scaling
Concurrency Scaling is a feature designed to support large numbers of concurrent users and queries. You are charged only for the time queries are actively running. Each clusters receives up to one hour of free Concurrency Scaling credits daily. Any usage that exceeds the free credits is subject to charges on a per second on-demand rate.  

### Redshift ML
This functionality enables you to create, train, and deploy machine learning (ML) models. The CREATE MODEL request may accrue additional costs on S3. Charges are typically minimal and should be less than $1 a month. 

## Reserved Instances
[Reserved Instances](/aws/concepts/reserved-instances) are covered in depth under General Concepts and we encourage you to read up more on them there for the most up-to-date information.

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-1szz6puz7-zRuJ8J4OJIiBFlcTobYZXA).