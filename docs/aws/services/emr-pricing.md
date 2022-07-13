title: EMR Pricing | Cloud Cost Handbook

[Amazon EMR Pricing Page](https://aws.amazon.com/emr/pricing/){ .md-button }

## Summary

Amazon Elastic Map Reduce (EMR) is software infrastructure for running map reduce and other big data workloads. It supports open-source frameworks like Apache Spark, projects like Hadoop, and SQL tools like Presto.

EMR runs on top of EC2 or EKS instances and also has a serverless option. EMR is available for a wide variety of instances which allows for tight optimization of workloads, for example choosing a compute optimized vs. a memory optimized instance for Spark vs. Hive.

To see which EC2 instances are available for EMR, you can add the `On EMR` and `EMR Cost` columns on [ec2instances.info](https://instances.vantage.sh).

## Pricing Dimensions

EMR is billed differently based on the underlying compute service.

| Dimension      | Description                                                                                                                                                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Running on EC2 | EMR is billed as an additional cost per hour for the instance. For example, a [m6g.16xlarge](https://instances.vantage.sh/aws/ec2/m6g.16xlarge.html) has an EMR cost of ~$0.60 per hour. |
| Running on EKS | Running on EKS involves 2 dimensions: vCPUs and GiB of memory, with a minimum charge of 1 minute.                                                                                        |
| Serverless     | Serverless has Compute, Memory, and Storage dimensions.                                                                                                                                  |

## EMR Optimization

Every EMR instance above can also be run as a spot instance, which is likely to be appropriate for "fault tolerant" workloads on EMR. As of 2020, it is also possible to use Spot Fleets with the [capacity-optimized allocation strategy](https://aws.amazon.com/blogs/big-data/optimizing-amazon-emr-for-resilience-and-cost-with-capacity-optimized-spot-instances/) for running EMR workloads. Lastly, data transfer charges are likely accumulating from the movement of your big data through the EMR system. You can dramatically reduce these charges, or even eliminate them, by connecting to EMR using [interface VPC endpoints](https://docs.aws.amazon.com/emr/latest/ManagementGuide/interface-vpc-endpoint.html).

!!! Contribute
Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-oey52myv-gq4AWRKkX25kjp1UGziPTw).
