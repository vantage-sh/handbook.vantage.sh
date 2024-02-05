title: Config Pricing | Cloud Cost Handbook

[Amazon Config Pricing Page](https://aws.amazon.com/config/pricing/){ .md-button target="_blank"}

## Summary
AWS Config is a service used to record and monitor configuration items in your AWS environment, and then evaluate them using Config rule evaluations. A configuration item is recorded when a monitored resource changes. Resources are AWS entities like EC2 instances, S3 buckets, and IAM roles. You can then apply compliance checks and policies using Config rules.

Its most common use case is for compliance monitoring to ensure that your AWS resources adhere to security and operational best practices. However, it is also used for resource administration, managing and troubleshooting configuration changes, and security analysis.

## Pricing Dimensions
| Dimension                       | Description |
| ------------------------------  | ----------- |
| Configuration Item Recordings | The rate is $0.003 for each configuration item recorded. |
| Config Rule Evaluations | See the [Config Rule Evaluations](#config-rule-evaluations) section for more information. |
| Conformance Pack Evaluations | See the [Conformance Pack Evaluations](#conformance-pack-evaluations) section for more information. |
| S3 Storage | Additional [S3](/aws/services/s3-pricing) costs could occur for snapshots and history files. |
| SNS Charges | You will incur additional charges if you opt into SNS notifications. | 
| Lambda Charges | If you create custom rules that use [Lambda](/aws/services/lambda-pricing) functions for evaluation, you will incur Lambda charges based on usage. |

## Config Rule Evaluations

With Config, you can create Config rules or use the predefined rules (called managed rules) that reflect your desired configurations. These rules are continuously monitored for compliance, with any deviations flagged as noncompliant by Config. You are charged per Config rule evaluation on a tiered model, with evaluations getting less expensive the more there are. After 500,000 evaluations you are no longer charged.

## Conformance Pack Evaluations
Conformance pack evaluations occur when a resource is evaluated by a Config rule within a conformance pack. A conformance pack is a "collection of AWS Config rules and remediation actions." Charges are per conformance pack evaluation on a tiered basis, with the cost decreasing as more evaluations occur.

## Config Cost Optimization Tips
[AWS recommends](https://aws.amazon.com/blogs/mt/cost-optimization-recommendations-for-aws-config/) a few tips for cost optimization:

- Only select from the resources needed when configuring Config.
- Only monitor resources in the regions that are necessary for your specific use case.
- Set up a lifecycle policy to auto-delete configuration history records after a specified number of days in order to reduce storage costs. 
- Customize conformance packs to ensure there are no duplicate rules.

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Oct 6, 2023_
