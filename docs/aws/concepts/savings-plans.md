title: Savings Plans

Savings Plans are a flexible pricing model offering discounted prices compared to On-Demand pricing, in exchange for a specific usage commitment. Savings Plans are typically the highest impact, lowest effort way of realizing savings on your AWS account. They are roughly the same concept as [Reserved Instances](../reserved-instances) but offer greater flexiblity as they 1) can be utilized across multiple compute services (i.e., EC2 _and_ Fargate) and 2) you aren't locked into a specific instance family. Similar to Reserved Instances, there are greater discounts for prepaying for a longer term.

After purchasing a Savings Plan, AWS Billing will automatically apply savings as corresponding on-demand resources match the conditions of your Savings Plans. Savings Plans are only applicable to usage across Amazon EC2, AWS Lambda, and AWS Fargate. Machine Learning Savings Plans (sometimes called SageMaker Savings Plans) are available for Sagemaker. Typically, customers will use Savings Plans for these services and [Reserved Instances](/aws/concepts/reserved-instances/) for other services that aren't covered such as RDS and ElastiCache.

!!! Contribute
Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-oey52myv-gq4AWRKkX25kjp1UGziPTw).
