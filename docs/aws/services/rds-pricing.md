title: RDS Pricing | Cloud Cost Handbook

[Amazon RDS Pricing Page](https://aws.amazon.com/rds/pricing/){ .md-button }

## Summary

Amazon Relational Database Service (RDS) provides you with the ability to create databases running certain software such as MySQL, Postgres, SQL Server and more. RDS instances ultimately are preconfigured EC2 instances running certain managed database software. As a result, you'll see similarities between instance types for RDS and EC2 where RDS instances are prefixed with "db."

## Pricing Dimensions

|Dimension|Description|
|----|----|
|Instance Type Usage|RDS instance types are billed at an hourly rate and charged that hourly rate on a per-second basis for your usage.|
|Database Software|As RDS allows you to run different types of database software there are varying costs depending on which database software you choose to use. For example you can run Oracle and MySQL database on the same RDS instance types but they have different pricing as Oracle licensing contributes a higher cost than MySQL.| 
|Availability|RDS allows you to run RDS instances in either "Single AZ" or "Multi AZ" deployments. "Multi AZ" deployments are more highly available but carry a larger cost.| 
|Attached Storage|RDS allows you to attach storage to RDS instances either as General Purpose Storage or Provisioned IOPS storage. Behind the scenes these are just managed EBS Volumes that RDS orchestrates on your behalf. However, on your monthly AWS bill these charges will show up under the RDS service and not under the EBS service.| 
|Backup Storage|You have the ability to turn on backups for your RDS instances and are charged an accompanying storage rate for backups.| 

## Reserved Instances

As RDS instances are **not** covered by [AWS Savings Plans](/aws/concepts/savings-plans/), you must rely on procuring [Reserved Instances](/aws/concepts/reserved-instances/) specifically for RDS. Reserved Instances are covered in depth under General Concepts and we encourage you to read up more on them there for the most up-to-date information.

## Single vs Multi Availability Zones

RDS allows you to deploy instances in either a single availability zone or across multiple availability zones. Shorthand, this is referenced as either "single-AZ" or "multi-AZ". The benefit of being multi-AZ is that you're provided with enhanced availability and durability for your database as Amazon provisions and maintains a standby in a different availability zone for automatic failover in the event of a scheduled or unplanned outage. 

From a cost consideration perspective, multi-AZ rates are double what single-AZ rates are for the added durability that you're provided. 

<br/>

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-1szz6puz7-zRuJ8J4OJIiBFlcTobYZXA).
