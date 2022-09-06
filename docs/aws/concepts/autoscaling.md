title: Autoscaling 

The best way to optimize costs in the cloud is to not spend it in the first place. Enter Autoscaling. Autoscaling leverages the elasticity of the cloud to dynamically provision and remove capacity based on demand. That means that as demands decrease autoscaling will automatically scale down resources and allow you to save on costs accordingly. 

Autoscaling applies to a variety of different services, some of which are described in more detail below. If you're looking for EC2 autoscaling concepts, please see the AWS EC2 service page for the [autoscaling section](/aws/services/ec2-pricing/#autoscaling).


## Application Autoscaling

For other resources in AWS, [Application Autoscaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) provides the ability to adjust provisioned resources.

Application Autoscaling supports the following services:

* AppStream 2.0 fleets
* Aurora replicas
* Amazon Comprehend document classification and entity recognizer endpoints
* [DynamoDB](/aws/services/dynamodb-pricing/) tables and global secondary indexes
* [Amazon Elastic Container Service (ECS)](/aws/services/ecs-and-fargate-pricing/) services
* Amazon EMR clusters
* Amazon Keyspaces (for Apache Cassandra) tables
* [Lambda](/aws/services/lambda-pricing/) function provisioned concurrency
* Amazon Managed Streaming for Apache Kafka (MSK) broker storage
* SageMaker endpoint variants

## Autoscaling Strategies

There are various methods by which autoscaling can occur. These are listed below in no partiuclar order:

* **Target Scaling** adds or removes capacity to keep a metric as near a specific value as possible. For example, target average CPU utilization of 50% across a set of ECS Tasks. If CPU utilization gets too high, add nodes. If CPU utilization gets too low, remove nodes.
* **Step Scaling** will adjust capacity up and down by dynamic amounts, depending on the magnitude of a metric.
* **Scheduled Scaling** will adjust mininmum and maximum capacity settings on a schedule.
* **Simple Scaling** will add or remove EC2 instances from an Autoscalng Group when an alarm is in alert state.
* **Predictive Scaling** can leverage historical metrics to preemptively scale EC2 workloads based on daily or weekly trends.
* **Manual Scaling** is possible with EC2 instances if teams need to intervene with an autoscaling group. This allows you to manually adjust the autoscaling target without any automation. 

## Other Considerations

Adding capacity is generally an easy process. For compute, it's just a matter of launching new workers from static images or automated standup processes.

Reducing capacity can be tricky depending on the application. Web applications generally have their requests clean up to prepare for termination within 30 seconds. Load balancers are often used to drain requests off instances and then terminate the instances "cleanly". Queue/batch workers, on the other hand, need to be done with their work, or stash their work somewhere before the node can be terminated. Otherwise, requests and/or data can be lost or incomplete.

DynamoDB Provisioned Capacity has [restrictions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) regarding how frequently it can be reduced (4 times per day at any time, plus any time when there hasn't been a reduction in the last hour). There are no restrictions regarding increasing capacity. Tables and Secondary Indexes are managed/scaled independently.

Scaling cooldown can be the trickiest part of the process. It's generally best to aggressively scale up/out and conservatively scale down/in. A long cooldown process might be necessary when scaling out an application with a long startup process, but it can also block future scale out events, resulting in application instability. Scaling policies should be regularly evaluated and tuned.

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-oey52myv-gq4AWRKkX25kjp1UGziPTw).

