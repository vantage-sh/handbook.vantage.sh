title: I/O Operations (IOPS) on AWS | Cloud Cost Handbook

## I/O Operations

I/O Operations (IOPS) are a relatively low level unit in AWS for measuring disk performance. The maximum size of an IOP is 256 KiB for SSD volumes and 1 GiB for HDD volumes. 1 GiB of storage is worth 3 IOPS so a 1,000 GiB EBS Volume has 3,000 IOPS available. When using these volume types you are charged for the amount of provisioned iops even if you don't fully utilize them.

As indidicated on the [EBS](/aws/services/ebs-pricing) page:

> Provisioned IOPS SSD volumes use a consistent IOPS rate, which you specify when you create the volume, and Amazon EBS delivers the provisioned performance 99.9 percent of the time.

The ["performance consistency"](https://blog.maskalik.com/blog/2020/05/31/aws-rds-you-may-not-need-provisioned-iops/) between a Provisioned IOPS volume and a general prupose (`gp2`, `gp3`), throughput optimized (`st1`), or cold HDD (`sc1`) is going to be better for both random and sequential disk access. Note that for operations with "large and sequential" accesses, provisioned iops are likely less efficient than an `st1` volume.

## IOPS Considerations

- **Volume Type** There are multiple volume types with different impacts on IOPS.
- **I/O Demand** Most likely the workload has a bursty demand pattern, where consistently high throughput is not as important as meeting spikes of demand. As the workload deviates from this, provisioned IOPS become more important.
- **Throughput Limits** The instance will have an upper limit of throughput it can support. For example, an [i2.xlarge](https://instnaces.vantage.sh/aws/ec2/i2.xlarge.html) can support up to 62,500 IOPS. If the number of Provisioned IOPS is even higher than this limit, it is a waste because the instance cannot use them all up.

## Optimal Provisioned IOPS

The most common cost waste with IOPS is having too many of them. It is commonly believed that the key to [RDS](/aws/services/rds-pricing/) is to have some amount of Provisioned IOPS. Happily, we do not have to guess.

AWS [suggests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-io-characteristics.html) inspecting the `VolumeQueueLength` metric for [CloudWatch](/aws/services/cloudwatch-pricing/). This metric is reported as IOPS, which means the formula is simple: if `VolumeQueueLength` is greater than the number of provisioned IOPS and latency is an issue, then you should consider increasing the number of provisioned IOPS.

!!! Contribute
Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-oey52myv-gq4AWRKkX25kjp1UGziPTw).
