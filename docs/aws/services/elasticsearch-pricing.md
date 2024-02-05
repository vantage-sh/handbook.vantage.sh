title: Elasticsearch Service Pricing | Cloud Cost Handbook

[Amazon Elasticsearch Service Pricing Page](https://aws.amazon.com/what-is/elasticsearch){ .md-button target="_blank"}

## Summary

Amazon Elasticsearch Service is a fully managed service that runs [Elasticsearch](https://www.elastic.co/elastic-stack/) which is used primarily for querying JSON-based search and analytics data. Amazon Elasticsearch Service is billed per instance for the amount of EBS storage attached to the instance and the type of instance that is used to run the service.

## Pricing Dimensions

|Dimension|Description|
|----|----|
|Instance Type Usage|Elasticsearch instance types are billed at an hourly rate and charged that hourly rate on a per second basis for your usage.|
|Attached Storage|Elasticsearch allows you to attach storage to the instances either as General Purpose Storage or Provisioned IOPS storage. Behind the scenes these are just managed EBS Volumes that Elasticsearch orchestrates on your behalf. However, on your monthly AWS bill these charges will show up under the Elasticsearch service and not under the EBS service. There are also options for high performance local SSD disks for storage optimized instances.|

## Storage Optimized Instances
If better storage performance, above EBS, is needed you can select Storage Optimized instances which include local NVMe SSD disks.

## Reserved Instances

As Elasticsearch instances are **not** covered by [AWS Savings Plans](/aws/concepts/savings-plans/), you must rely on procuring [Reserved Instances](/aws/concepts/reserved-instances/) specifically for Elasticsearch. Reserved Instances are covered in depth under General Concepts and we encourage you to read up more on them there for the most up-to-date information.

<br/>

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Jul 19, 2021_
