The best way to optimize costs in the cloud is to not spend it in the first place. Enter Autoscaling. Autoscaling is leveraging the elasticity of the cloud to dynamically provision and remove capacity based on demand.

## EC2 Autoscaling

EC2 autoscaling is provided by [Autoscaling Groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html). Autoscaling groups have [lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) to accommodate complex workflows regarding instance creation or termination and can support multiple instance types or spot instances using a [Mixed Instance Policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html). New instances are added based on a launch template (or launch config). This can be a challenge for organizations without good practices around creating machine images or automation for standing up applications.

## Application Autoscaling

For other resources in AWS, [Application Autoscaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) provides the ability to adjust provisioned resources.

Application Autoscaling supports the following services:

* AppStream 2.0 fleets
* Aurora replicas
* Amazon Comprehend document classification and entity recognizer endpoints
* DynamoDB tables and global secondary indexes
* Amazon Elastic Container Service (ECS) services
* Amazon EMR clusters
* Amazon Keyspaces (for Apache Cassandra) tables
* Lambda function provisioned concurrency
* Amazon Managed Streaming for Apache Kafka (MSK) broker storage
* SageMaker endpoint variants

## Scaling Strategies

* **Target Scaling** adds or removes capacity to keep a metric as near a specific value as possible. For example, average CPU utilization of 50% across a set of ECS Tasks.
* **Step Scaling** will adjust capacity up and down by dynamic amounts, depending on the magnitude of a metric.
* **Scheduled Scaling** will adjust min/max capacity settings on a schedule.
* **Simple Scaling** will add or remove EC2 instances from an Autoscalng Group when an alarm is in alert state.
* **Predictive Scaling** can leverage historical metrics to preemptively scale EC2 workloads based on daily or weekly trends.
* **Manual Scaling** is possible with EC2 instances, if teams need to intervene with an autoscaling group.

## Other Considerations

Adding capacity is generally an easy process. For compute, it's just a matter of launching new workers from static images or automated standup processes.

Reducing capacity can be tricky, depending on the application. Web apps generally have their requests clean up inside 30 seconds, so it's easy to use load balancers to drain requests off instances and then terminate cleanly. Queue/batch workers, on the other hand, need to be done with their work, or stash their work somewhere before the node can be terminated. Otherwise, requests can be lost.

DynamoDB Provisioned Capacity has [restrictions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) regarding how frequently it can be reduced (4 times per day at any time, plus any time when there hasn't been a reduction in the last hour). There are no restrictions regarding increasing capacity. Tables and Secondary Indexes are managed/scaled independently.

Scaling cooldown can be the trickiest part of the process. It's generally best to aggressively scale up/out and conservatively scale down/in. A long cooldown process might be necessary when scaling out an application with a long startup process, but it can also block future scale out events, resulting in application instability. Scaling policies should be regularly evaluated and tuned.

!!! Contribute
    Help us improve this page by making a contribution on our [Github repository](https://github.com/vantage-sh/handbook).

