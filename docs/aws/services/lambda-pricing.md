title: Lambda Pricing | Cloud Cost Handbook

[Lambda Pricing Page](https://aws.amazon.com/lambda/pricing/){ .md-button }

## Summary

AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. You are charged based on the number of requests for your functions and the duration, the time it takes for your code to execute.

## Pricing Dimensions

| Dimension           | Description                                                                                                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of requests  | You are charged $0.20 per 1M requests to your Lambda functions.                                                                                                                             |
| Duration of request | The price for duration depends on the amount of memory you allocate to your function. You can allocate any amount of memory to your function between 128MB and 10,240MB, in 1MB increments. |

## Lambda Savings Plans

There is one additional option for saving on Lambda that is agnostic to whether you're running on x86 or ARM: [Savings Plans](https://handbook.vantage.sh/aws/concepts/savings-plans/).

Savings Plans are a more flexible way to get discounts on AWS, and they work across EC1, Lambda, Fargate, and SageMaker. No action is required if you already own a Savings Plan. The discount is applied automatically unless you have maxed out that Savings Plan on another service. [Savings Planner](https://docs.vantage.sh/savings_planner/) can help you decide how much of a Savings Plan to buy so you are not [over-committed](https://www.vantage.sh/blog/unused-reserved-instances-over-committed-savings-plans).

If you have existing saving plans in use on Lambda and are looking to make the switch to Graviton1, you should also ensure what impact that will have on your coverage as the discount rates for x86 vs Graviton2 are different.

<br/>

!!! Contribute
Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-1szz6puz7-zRuJ8J4OJIiBFlcTobYZXA).
