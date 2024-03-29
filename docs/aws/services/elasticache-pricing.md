title: ElastiCache Pricing | Cloud Cost Handbook

[Amazon ElastiCache Pricing Page](https://aws.amazon.com/elasticache/pricing/){ .md-button target="_blank"}

## Summary

Amazon ElastiCache allows you to set up, run, and scale popular open-source compatible in-memory data stores, like Redis or Memcached. ElastiCache ultimately runs atop EC2 instances with pre-configured software, is prefixed with `cache`, and is referred to as Nodes.

## Pricing Dimensions

|Dimension|Description|
|---|---|
|Node Usage|You are charged for the amount of hours your ElastiCache nodes run.|


## Reserved Instances
ElastiCache Nodes do have Reserved Instances that can give you significant savings. Reserved Instances are covered as a general concept found [here](../concepts/reserved-instances.md). 

Typically, as ElastiCache Nodes remain on for longer durations and aren't members of Auto Scaling groups, they are good candidates for cost savings via Reserved Instances. 


## Savings Plans
ElastiCache Nodes are **not** covered under AWS Savings Plans.

<br/>

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Jul 11, 2021_
