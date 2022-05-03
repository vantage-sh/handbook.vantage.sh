title: EBS Pricing | Cloud Cost Handbook

[Amazon EBS Pricing Page](https://aws.amazon.com/ebs/pricing/){ .md-button }

## Summary

Amazon Elastic Block Storage (EBS) is amazon's block storage offering that allows you to create "Volumes" which is the base primitive of everything related to EBS. There are multiple EBS "Volume Types" that offer different capabilites and have their own set of pricing. EBS costs are factored into the cost category of "EC2-Other" on your AWS bill which can oftentimes complicate understanding where these costs are coming from. 

It is important to note that you are charged for the amount of _provisioned_ storage not _utilized_ storage. So, for example, if you create a 20GB EBS Volume and only utilize 1GB of it, you are still charged for all 20GB. 

## Pricing Dimensions

| Dimension | Description |
|--------|--------|
| Volume Storage Hours | When you create an EBS Volume you allocate a certain amount of storage to it. Ultimately the main cost of an EBS Volume is the result of the amount of hours you're using an EBS Volume and the size you allocate. |
| Volume Type | EBS has different types of Volume Types which are documented below. Each Volume Type has different rates. |
| Provisioned IOPS | Certain EBS Volume types (io2, io2) allow you to specific an amount of provisioned input/output operations per second which is abbreviated as IOPS and pronounced as "eye-ops". When using these volume types you are charged for the amount of provisioned iops even if you don't fully utilize them. |
| Amazon EBS Snapshots | Amazon EBS Snapshots are a point in time copy of your block volume data. EBS Snapshots are stored incrementally, which means you are billed only for the changed blocks stored. |
| EBS Snapshot API Requests | EBS charges you for the amount of API calls you make for snapshots. These are charged in increments of thousands of API requests. | 


## Volume Types

Amazon EBS offers a few different Volume Types that have different pricing rates and functionality. Each EBS Volume Type is described below:

| Volume Type | Description |
|------|-----|
| General Purpose SSD (gp2, gp3) | General Purpose SSD (gp3) volumes offer cost-effective storage that is ideal for a broad range of workloads. |
| Provisioned IOPS (io1, io2) | Provisioned IOPS SSD (io1 and io2) volumes are designed to meet the needs of I/O-intensive workloads, particularly database workloads, that are sensitive to storage performance and consistency. Provisioned IOPS SSD volumes use a consistent IOPS rate, which you specify when you create the volume, and Amazon EBS delivers the provisioned performance 99.9 percent of the time. |


## Stranded Volumes

Oftentimes, EBS Volumes are created in conjunction with other AWS resources such as EC2 instances but are de-coupled from the lifecycle of those other resources. One common pattern we see is that developers will create EC2 instances with EBS Volumes attached but when they delete the EC2 instance, they assume that the EBS Volume is destroyed accordingly. In larger-scale environments with autoscaling this problem can grow significantly as a part of an AWS bill.

We recommend that you periodically profile for unattached or stranded EBS Volumes.

<br/>

!!! Contribute
    Help us improve this page by contributing on [GitHub](https://github.com/vantage-sh/handbook) or discuss the handbook in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-oey52myv-gq4AWRKkX25kjp1UGziPTw).