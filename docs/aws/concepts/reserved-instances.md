Reserved Instances (oftentimes referred to as their abbreviation of RIs) are one of the most popular and high-impact cost reduction methods you can leverage for cutting your bill. Reserved Instances give you the ability to pay upfront for certain AWS services to receive a discount. As a result, if you are able to profile usage across your AWS account and know that you'll hit certain usage levels, Reserved Instances can typically save you money. 

Reserved Instances are availabile to a variety of AWS services such as [EC2](../services/ec2-pricing.md), [ElastiCache](../services/elasticache-pricing.md) and [RDS](../services/rds-pricing.md). AWS Billing automatically applies your Reserved Instance discounted rate when attributes of your instance usage match attributes of an active Reserved Instance. For general compute usage (EC2, Fargate, etc.), [Savings Plans](savings-plans.md) are _always_ preferred to Reserved Instances as they give you the same discount but are more flexible across all compute. 

It's important to note that Reserved Instances aren't actually separate instances. They are merely financial instruments that you buy and are automatically applied to your account. As a result, you can continue to spin up and use on-demand instances and purchase Reserved Instances concurrently. As on-demand instances match your Reserved Instance attributes, you'll automatically receive discounts. 

## Reserved Instance Term

AWS gives different discounts depending on the term that you pay upfront for. You can yield greater savings for paying upfront for longer terms but lose flexibility as a result. We find that smaller customers just getting started in their infrastructure journey tend to prefer 1-Year Reserved Instances whereas more mature organizations will leverage 3-Year Reserved Instances for the greatest savings as they can more accurately model and predict their usage. 

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-oey52myv-gq4AWRKkX25kjp1UGziPTw).