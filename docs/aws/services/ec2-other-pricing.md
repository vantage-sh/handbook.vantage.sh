## Summary

EC2-Other is a category of AWS costs that typically causes the greatest amount of confusion for customers as it doesn't necessarily map to a single AWS service. EC2-Other encompasses the following costs:

|Usage Type|Description|
|-----|-----|
|EBS Volume Usage|Usage for [EBS Volumes](ebs-pricing.md).|
|EBS Snapshot Usage|Usage for [EBS Snapshots](ebs-pricing.md).|
|CPU Credits from t2/t3/t4g EC2 instances|T-family EC2 Instances can carry potential CPU credit charges as described more below.|
|NAT Gateway Usage|Hourly usage for NAT Gateways.|
|Data Transfer| |
|Idle Elastic IP Address usage|AWS charges you for unattached IP addresses. It's typically good hygiene to occasionally monitor for stranded resources and clean them up.|

## Stranded Resources

Unused or stranded EBS Volumes and IP Addresses can add up over time especially if these resources are created automatically as part of an autoscaling service where they're spun up but not down. You should consider occasionally auditing your unattached EBS Volumes and IP addresses to see if you can clean them up to save costs.

## What are t2/t3/T4g CPU credit charges?

T2, T3 and T4g instances have a concept of "Unlimited mode" whereby you are charged a per-vCPU hour for bursting into this CPU usage. If you are leveraging these EC2 Instance Types with `unlimited` mode enabled, you should consider keeping an eye on these costs. Depending on how much your costs trend here, you may want to consider "[rightsizing](../concepts/rightsizing.md)" to a different instance type that is allocated additional CPU.

<br/>

!!! Contribute
	Help us improve this page by making a contribution on our [Github repository](https://github.com/vantage-sh/handbook).