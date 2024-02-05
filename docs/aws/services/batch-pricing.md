title: Batch Pricing | Cloud Cost Handbook

[AWS Batch Pricing Page](https://aws.amazon.com/batch/pricing/){ .md-button target="_blank" }

## Summary

AWS Batch combines job scheduling and job execution into one managed service. Example Batch workloads include video rendering, log file ingestion, model training, simulation, and cosmology. Under the hood, Batch provisions [EC2](/aws/services/ec2-pricing/) or [Fargate](/aws/services/ecs-and-fargate-pricing/) instances and executes containerized jobs on them.

Users set a range of vCPUs and memory that are needed to execute the job. You can also choose specific instance types, which can be helpful for cost optimizations. For both EC2 and Fargate jobs, it is possible to select on-demand or spot instances. Job execution itself can be managed with scheduling, allocation, and parallelization parameters.

## Pricing Dimensions

Batch is free!

AWS Batch only consumes the underlying EC2 or Fargate resources, however it does not break these out in the bill. If Batch is pointed at existing EC2 instances, or in other words the Batch Compute Environment is `UNMANAGED`, the cost of the Batch jobs will be the elapsed time they run on the instance.

To view the cost of a job in a `MANAGED` Batch environment, you must inspect the ECS tasks that are associated with it. You can view the cost of AWS batch jobs through ECS in [Cost Reports](/tools/cost-reports/).

Another technique is to add a [tag](/aws/concepts/tags/) to the [compute environment](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) that is created to run the Batch job. This does not allow you to track costs down to the job level.

## Where Jobs Should Run

One consideration is whether Batch is even the right tool for the job, and if so what compute type is preferred. The table below shows various options for running batch workloads on AWS, and the constraints that come with each.

|                           | Lambda                                               | Fargate (Spot)                   | Fargate                       | EC2 (Spot)  | EC2         |
| ------------------------- | ---------------------------------------------------- | -------------------------------- | ----------------------------- | ----------- | ----------- |
| Job Length            | <15 mins                                             | 5 - 10 mins                      | 5 - 10 mins                   | 5 - 45 mins | Hours       |
| Compute Limits        | [Lambda](/aws/services/lambda-pricing/) Runtime Only | <4 vCPUs, <30 GiB memory, no GPU | <4 vCPUS, <30 GiB mem, no GPU | None        | None        |
| Startup Time          | <1 sec                                               | 30 - 90 secs                     | 30 - 90 secs                  | 5 - 15 mins | 5 - 15 mins |
| Job is Fault Tolerant | No                                                   | Yes                              | No                            | Yes         | No          |

## Batch Cost Optimization Tips

[AWS recommends](https://aws.amazon.com/blogs/hpc/aws-batch-best-practices/) a few techniques to lower costs for Batch jobs:

- The most cost-effective [allocation strategy](https://aws.amazon.com/blogs/compute/optimizing-for-cost-availability-and-throughput-by-selecting-your-aws-batch-allocation-strategy/) for non-interruptible workloads is `BEST_FIT`. This strategy is sensitive to capacity constraints however and so an entire workload may have to wait for available machines. To avoid this, `BEST_FIT_PROGRESSIVE` tries to find the best instances but falls back to less cost-efficient instances that will still complete the job (e.g. have the minimum required number of vCPUs). For Fargate and EC2 Spot workloads, `SPOT_CAPACITY_OPTIMIZED` uses the same Auto Scaling algorithm as Spot Fleets to get the best price.
- Use smaller containers and image layers. Loading each container consumes compute time for the job. Furthermore, pulling containers across [NAT Gateways](/aws/services/vpc-pricing/#nat-gateway) will rack up data transfer charges. Prefer PrivateLink for pulling containers.
- Use multiple availability zones. All things considered, `BEST_FIT_PROGRESSIVE` will find the cheapest AZ to run the workload in, so do not artificially limit yourself here.

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Sep 1, 2022_