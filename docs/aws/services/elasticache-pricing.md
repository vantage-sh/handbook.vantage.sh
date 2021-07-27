title: ElastiCache Pricing | Vantage Cloud Cost Handbook

[Amazon ElastiCache Pricing Page](https://aws.amazon.com/elasticache/pricing/){ .md-button }

## Summary

Amazon ElastiCache allows you to set up, run, and scale popular open-source compatible in-memory data stores like Redis or Memcached. ElastiCache ultimately runs atop EC2 instances with pre-configured software and are prefixed with `"cache."` and are referred to as Nodes.

## Pricing Dimensions

* **Node Usage**: You are charged for the amount of hours your ElastiCache nodes run.


## Reserved Instances
ElastiCache Nodes do have Reserved Instances that can give you significant savings. Reserved Instances are covered as a general concept found [here](../concepts/reserved-instances.md). 

Typically, as ElastiCache nodes remain on for longer durations and aren't members of auto-scaling groups, they are good candidates for cost savings via Reserved Instances. 


## Savings Plans
ElastiCache Nodes are **not** covered under AWS Savings Plans.

<br/>

!!! Contribute
	Help us improve this page by making a contribution on our [Github repository](https://github.com/vantage-sh/handbook).