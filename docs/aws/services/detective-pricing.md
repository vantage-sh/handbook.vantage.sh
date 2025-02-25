title: Detective Pricing | Cloud Cost Handbook

[Amazon Detective Pricing Page](https://aws.amazon.com/detective/pricing){ .md-button target="_blank"}

## Summary

Amazon Detective is a security service that automatically collects log data from AWS resources and uses machine learning, statistical analysis, and graph theory to build a linked set of data that enables you to investigate potential security issues.

Amazon Detective pricing is based on the amount of data ingested for analysis. There is no additional charge for the use of the Amazon Detective service itself, such as investigations, or for storing the findings (Amazon Detective stores the findings for 12 months).

It does not currently provide any mechanism to select the type of data to ingest, so all sources will be ingested when enabled. Current sources includes VPC Flow Logs, AWS CloudTrail logs, Amazon Elastic Kubernetes Service (Amazon EKS) audit logs, AWS Security Hub findings, and Amazon GuardDuty findings.

CloudWatch Logs are not ingested directly, therefore Amazon Detective does not analyse application level logging and is just for logs generated automatically by AWS resources.

## Pricing Dimensions

|Dimension|Description|
|----|----|
|Data Ingestion|Amazon Detective pricing is based on the amount of data ingested into the service. Data ingestion is measured in gigabytes (GB) per month and cost per GB varies by region.|

## Organization Accounts

When using [AWS Organizations](https://aws.amazon.com/organizations/){ target="_blank"} there is typically a centralised security or management account which is delegated as the "Administrator account" to perform the analysis and view the results of Amazon Detective. The Amazon Detective charges will still be associated with the individual organization account the ingested logs relate to, and not the centralised account which is performing the analysis.

Pricing varies by region and is dependent on the origin region of the log data being ingested.

<br />

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Feb 25, 2025_
