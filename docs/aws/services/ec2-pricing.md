[Amazon EC2 Pricing Page](https://aws.amazon.com/ec2/pricing/)

## Summary

Amazon EC2 (Elastic Cloud Compute) is Amazon’s most popular service and usually one of the top cost centers for most companies. Amazon EC2 allows customers to create virtual private servers and has different pricing depending on the “instance type” you use. Instance types are grouped into families with varying generations. Each instance type has a different mix of underlying hardware, allocated resources and as a result: pricing. Additionally, depending on the underlying software running on the EC2 instance you may be charged different rates.

## Pricing Dimensions

* **Instance Type Usage**: EC2 instance types are billed on one second increments, with a minimum of 60 seconds. For certain instance types with pre-installed software, you are billed in increments of hours. 
* **Instance Type Lifecycle**: EC2 has different lifecycle types - the two most often used are on-demand and spot. These concepts are discussed more in-depth below. 
* **AMI**: AMI stands for Amazon Machine Images. Depending on the AMI you use (i.e., Linux vs Windows) you potentially pay an additional amount of money on top of the instance type base usage. 

## On-Demand vs Spot

## Rightsizing
Rightsizing refers to the process of ensuring that you're using the proper instance type suited for your application or workload. For example if you're using the largest instance type in a particular family but not using the CPU, Storage and Memory allocated to it fully you may be overpaying for what you need. Rightsizing is usually a manual process that involves engineering time for looking at a combination of application-level performance metrics like application CPU and Memory consumption and infrastructure-related attributes like what kind of underlying CPU powers an instance type. 

## Savings Plans
EC2 Instances are covered by AWS Savings Plans. Savings Plans are covered more in depth as a general concept [here](/aws/concepts/savings-plans/). 

## Reserved Instances

## Instance Type Families