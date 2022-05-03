title: ECS & Fargate Pricing | Cloud Cost Handbook

[ECS Pricing Page](https://aws.amazon.com/ecs/pricing/){ .md-button }
[Fargate Pricing Page](https://aws.amazon.com/fargate/pricing/){ .md-button }

## Summary

Elastic Container Service (ECS) allows you to run docker containers through a primitive named a "Task". Tasks ultimately run on EC2 instances which are either managed by you (ECS on EC2) or fully managed by AWS (Fargate).

There is no additional charge to you when using ECS on self-managed EC2 as you're just paying for EC2 instances that you create and manage. Fargate charges you for the vCPU and Memory for a ECS Task or EKS Pod and you pay a premium for managing the underlying EC2 instances. 

## Fargate Pricing Dimensions

|Dimension|Description|
|---|---|
|vCPU Hours|When configuring a Fargate Task or EKS Pod you assign a certain amount vCPU and are charged a corresponding per-hour VCPU rate.|
|GB Memory Hours|When configuring a Fargate Task or EKS Pod you assign a certain amount GB of Memory and are charged a corresponding per-hour GB of Memory rate.|

### Fargate Spot

Fargate has the ability to run in a Spot capacity which is conceptually the same premise as [EC2 Spot](/aws/services/ec2-pricing/#on-demand-vs-spot) - allowing you to run Tasks at up to a 70% discount off the Fargate on-demand price. 

When the capacity for Fargate Spot is available, you will be able to launch tasks based on your specified request. When AWS needs the capacity back, tasks running on Fargate Spot will be interrupted with two minutes of notification. If the capacity for Fargate Spot stops being available, Fargate will scale down tasks running on Fargate Spot while maintaining any regular tasks you are running.

### Fargate vs self-managed EC2 on ECS or EKS

Fargate charges a significant premium for managing the underlying nodes. Additionally, Fargate has varying degress of vCPU performance that differ depending on the Task. As a result, Fargate can have pitfalls relative to self-managed ECS or EKS on EC2 beyond just the additional costs. 

For a more in-depth article for seeing how Fargate is priced relative to self-managed EC2, please read the following blog post for [understanding Fargate pricing](https://www.vantage.sh/blog/fargate-pricing).

<br/>

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-oey52myv-gq4AWRKkX25kjp1UGziPTw).