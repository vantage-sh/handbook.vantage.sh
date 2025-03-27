title: Macie Pricing | Cloud Cost Handbook

[Amazon Macie Pricing Page](https://aws.amazon.com/macie/pricing){ .md-button target="_blank"}

## Summary

Amazon Macie is a security service for Amazon S3 that uses machine learning to automatically discover, classify, and protect sensitive data in Amazon S3.

More specifically, it scans for sensitive data such as personally identifiable information (PII), financial information, and intellectual property.

Pricing is based on the number of buckets monitored, the amount of S3 data scanned, and the number of objects discovered automatically when automated data discovery is enabled.

## Pricing Dimensions

|Dimension|Description|
|----|----|
|Number of S3 Buckets Monitored or Scanned|Amazon Macie charges a fixed monthly cost per bucket that is monitored or scanned|
|S3 Data Scanned|Amazon Macie has a tiered per GB charge based on the amount of S3 data scanned for sensitive data. Pricing varies by region.|
|Automated Data Discovery|Amazon Macie charges a monthly cost per 100k objects discovered, in addition to scanning, charges when automated data discovery is enabled. Pricing varies by region.|

## Macie Considerations

To minimize costs, consider excluding buckets that are known to not contain sensitive data that would be discovered by Amazon Macie (eg. VPC flow logs, CloudTrail logs and other auto-generated system logs).

For large buckets, consider running Macie on a subset of the data using random sampling over a percentage of the objects in a bucket. This is done by specifying the [sampling depth](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-create.html#discovery-jobs-create-step3){target=_blank} when creating a scan.

## Organization Accounts

When using [AWS Organizations](https://aws.amazon.com/organizations/){ target="_blank"} there is typically a centralised security or management account which is delegated as the "Administrator account" to manage the scans and view the results of Amazon Macie. The Amazon Macie charges will still be associated with the individual organization account the S3 buckets belong to, and not the centralised account being used for the analysis.

<br />

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Mar 27, 2025_
