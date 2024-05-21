title: EC2 Pricing | Cloud Cost Handbook

[Amazon EC2 Pricing Page](https://aws.amazon.com/ec2/pricing/){ .md-button target="_blank"}

## Summary

Amazon EC2 (Elastic Cloud Compute) is Amazon’s most popular service and usually one of the top cost centers for most companies. Amazon EC2 allows customers to create virtual private servers and has different pricing depending on the instance type you use. Instance types are grouped into families with varying generations. Each instance type has a different mix of underlying hardware, allocated resources, and as a result: pricing. Additionally, depending on the underlying software running on the EC2 instance you may be charged different rates.

## Pricing Dimensions

|Dimension|Description|
|------|-------|
| Instance Type Usage | EC2 instance types are billed on one second increments, with a minimum of 60 seconds. For certain instance types with pre-installed software, you are billed in increments of hours. |
| Instance Type Lifecycle | EC2 has different lifecycle types - the two most often used are on-demand and spot. These concepts are discussed more in-depth below. |
| Amazon Machine Images (AMI) | Depending on the AMI you use (i.e. Linux vs Windows) you potentially pay an additional amount of money on top of the instance type base usage. |

## On-Demand vs Spot

By default, EC2 instances are launched in On-Demand mode and charged accompanying on-demand rates (which are the most expensive). AWS also offers Spot Instances, which can offer significant cost savings by using unused additional compute capacity. However, Spot tends to only work for fault-tolerant workloads as AWS can pre-empt and terminate these instances within two minutes if need be. 

Depending on your application's needs, you can consider using Spot Instances for significant cost savings in the event you are comfortable with these instances being terminated. In general, your application's architecture should be comfortable with either (1) there being no Spot Instances available or (2) these instances being terminated. 

## Auto Scaling
EC2 [Auto Scaling](../../concepts/autoscaling/) is provided by a primitive named [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html). Auto Scaling groups have [lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) to accommodate complex workflows regarding instance creation or termination and can support multiple instance types or Spot Instances using a [Mixed Instance Policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html). New instances are added based on a launch template (or launch config). This can be a challenge for organizations without good practices around creating machine images or automation for standing up applications.


## Rightsizing
Rightsizing refers to the process of ensuring that you're using the proper instance type suited for your application or workload. For example, if you're using the largest instance type in a particular family but not using the CPU, storage, and memory allocated to it fully, you may be overpaying for what you need. Rightsizing is usually a manual process that involves engineering time for looking at a combination of application-level performance metrics like application CPU and memory consumption and infrastructure-related attributes like what kind of underlying CPU powers an instance type. 

## Savings Plans
EC2 instances are covered by AWS Savings Plans. Savings Plans are covered more in-depth as a general concept [here](/aws/concepts/savings-plans/). As it relates to EC2, Savings Plans are preferable as they present the same savings as Reserved Instances but aren't constrained to a single instance type. 

## Reserved Instances
EC2 instances are covered by AWS Reserved Instances. Reserved Instances are covered more in-depth as a general concept [here](/aws/concepts/reserved-instances/). As it relates to EC2, Reserved Instances aren't preferred as they present the same savings as Savings Plans but are constrained to a single instance type whereas Savings Plans give greater flexibility. 

## Instance Type Families
EC2 Instance Types are organized into families and each family can have multiple generations. By looking at each instance type you can infer its family and generation from the instance type name. For example, a `c5.4xlarge` is the `c` family and `5th` generation. Below is a table of EC2 Instance Families and simple descriptions:


| Family      | Description |
| ----------- | ----------- |
| a   | AMD(x86) Processor       |
| c   | Compute-optimized        |
| d   | Locally attached spinning HDD        |
| f   | Customizable hardware acceleration with FPGAs        |
| g   | Arm-based AWS Graviton2 processors        |
| h   | Large spinning HDD        |
| i   | Intel(x86) processor with NVMe SSD-backed storage optimized        |
| inf | Machine-learning inference |
| mac | Apple Mac mini computers |
| m   | General purpose with balanced CPU, memory and storage        |
| n   | Network performance optimzied |
| p   | General Purpose GPU |
| r   | Memory-optimized        |
| t   | Burstable instances        |
| x   | Lowest price-per-GB RAM instances        |
| z   | Highest core frequency        |

## Generational Upgrades
Typically, as cloud infrastructure providers release new generations for families, it's cheaper and more performant to run the later generation instance types. Upgrading instances from one generation to another can be a major area of cost savings. Generation upgrades usually result in between 5% and 10% cost savings per generation and vary per family. 

<br/>

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Aug 14, 2021_
