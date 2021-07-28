title: Elasticsearch Service Pricing | Vantage Cloud Cost Handbook

[Amazon Elasticsearch Service Pricing Page](https://aws.amazon.com/elasticsearch-service/pricing/){ .md-button }

## Summary

Amazon Elasticsearch Service is a full-managed service which runs [ElasticSearch](https://www.elastic.co/elastic-stack/) which is used primarily for querying JSOn based search and analytics data. Amazon ElasticSearch Service is billed per instance for the amount of EBS storage attached to the instance and the type of instance which is used to run the service.

## Pricing Dimensions

|Dimension|Description|
|----|----|
|Instance Type Usage|ElasticSearch instance types are billed at an hourly rate and charged that hourly rate on a per-second basis for your usage.|
|Attached Storage|ElasticSearch allows you to attach storage to the instances either as General Purpose Storage or Provisioned IOPS storage. Behind the scenes these are just managed EBS Volumes that ElasticSearch orchestrates on your behalf. However, on your monthly AWS bill these charges will show up under the ElasticSearch service and not under the EBS service. There are also options for high performance local SSD disks for storage optimized instances.|

## Storage Optimized Instances
If better storage performance, above EBS, is needed you can select Storage Optmized instances which include local NVMe SSD disks.

## Reserved Instances

As ElasticSearch instances are **not** covered by [AWS Savings Plans](/aws/concepts/savings-plans/), you must rely on procuring [Reserved Instances](/aws/concepts/reserved-instances/) specifically for ElasticSearch. Reserved Instances are covered in depth under General Concepts and we encourage you to read up more on them there for the most up-to-date information.

<br/>

!!! Contribute
	Help us improve this page by making a contribution on our [Github repository](https://github.com/vantage-sh/handbook).