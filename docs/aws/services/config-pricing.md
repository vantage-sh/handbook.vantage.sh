title: Config Pricing | Cloud Cost Handbook

[Amazon Config Pricing Page](https://aws.amazon.com/config/pricing/){ .md-button target="_blank"}

## Summary
AWS Config is a service used to record and monitor configuration items in your AWS environment, and then evaluate them using Config Rule Evaluations. A configuration item is recorded when a monitored resource changes. Resources are AWS entities like EC2 instances, S3 buckets, and IAM roles. You can then apply compliance checks and policies using Config rules.

Its most common use case is for compliance monitoring to ensure that your AWS resources adhere to security and operational best practices. However, it is also used for resource administration, managing and troubleshooting configuration changes, and security analysis.

## Pricing Dimensions
| Dimension                       | Description |
| ------------------------------  | ----------- |
| Configuration Item Recordings | The rate is $0.003 for each configuration item recorded. |
| Config Rule Evaluations | See the [Config Rule Evaluations Pricing](#config-rule-evaluations-pricing) section for more information. |
| Conformance Pack Evaluations | See the [Conformance Pack Evaluations Pricing](#conformance-pack-evaluations-pricing) section for more information. |
| S3 Storage | Additional [S3](/aws/services/s3-pricing) costs could occur for snapshots and history files. |
| SNS Charges | You will incur additional charges if you opt into SNS notifications. | 
| Lambda Charges | If you create custom rules that use [Lambda](/aws/services/lambda-pricing) functions for evaluation, you will incur Lambda charges based on usage. |

## Config Rule Evaluations Pricing

| AWS Config Rules Evaluations | Price Per Rule Evaluation Per Region |
| --- | --- |
| First 100,000 | $0.001 |
| Next 400,000 (100,001-500,000) | $0.0008 |
| Over 500,000 | $0.00 |

## Conformance Pack Evaluations Pricing
Conformance Pack Evaluations occur when a resource is evaluated by a Config rule within a Conformance Pack.

| Conformance Pack Evaluations | Price Per Conformance Pack Evaluation Per Region |
| --- | --- |
| First 100,000 | $0.001 |
| Next 400,000 (100,001-500,000) | $0.0008 |
| Over 500,000 | $0.0005 |

## Config Cost Optimization Tips
[AWS recommends](https://aws.amazon.com/blogs/mt/cost-optimization-recommendations-for-aws-config/) a few tips for cost optimization:

- Only select from the resources needed when configuring Config.
- Only monitor resources in the regions that are necessary for your specific use case.
- Set up a lifecycle policy to auto-delete configuration history records after a specified number of days in order to reduce storage costs. 
- Customize Conformance Packs to ensure there are no duplicate rules.

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).
