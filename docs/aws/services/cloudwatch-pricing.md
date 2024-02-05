title: CloudWatch Pricing | Cloud Cost Handbook

[Amazon CloudWatch Pricing Page](https://aws.amazon.com/cloudwatch/pricing/){ .md-button target="_blank"}

## Summary

Amazon CloudWatch is a logging, monitoring, and observability service. As with most monitoring and observability tools, the cost of service is based on the amount of data that is collected and stored, as well as a number of other factors. CloudWatch is no different. For most use cases, the largest CloudWatch costs are made up of the number of metrics and logs that a user is ingesting and storing. 

Oftentimes, CloudWatch is leveraged automatically by other AWS services for metric and log storage. Users are sometimes surprised when they spin up a number of unrelated services which they accounted for during planning, but are then greeted with an accompanying spike in CloudWatch costs that they didn't account for.

CloudWatch stores and processes data from an umbrella of different AWS services which means that sometimes it isn't obvious why the overall CloudWatch bill has increased. Diving into subcategory costs can help shed light on which other AWS services are causing CloudWatch costs to increase.

## Pricing Dimensions

| Dimension | Description |
| -------- | -------- |
| Custom Metric Storage | AWS charges you for the number of custom metrics you store with them per month. CloudWatch's unit pricing is progressive; the first 10,000 metrics tracked is $0.30 per metric per month, the next 240,000 costs $0.10 and so on.[^1] This gives users with large numbers of metrics automatic economies of scale as they grow the number of metrics tracked. Note: Pricing is dependant on the region where you store your metrics.[^2] |
| CloudWatch API Requests | AWS charges you for the following API requests: `GetMetricData`, `GetInsightRuleReport`, `GetMetricWidgetImage`, `GetMetricStatistics`, `ListMetrics`, `PutMetricData`, `GetDashboard`, `ListDashboards`, `PutDashboard` and `DeleteDashboards`. For most AWS services there is no API charge for sending metrics. A user would normally be charged by the CloudWatch API for ingesting metrics from a non-AWS service or for a third-party infrastructure monitoring/observability tool reading from the API to collect metrics. Pricing is dependant on the region where CloudWatch is deployed.[^3] |
| CloudWatch Dashboards | AWS charges $3.00 per month per CloudWatch dashboard.  |
| CloudWatch Alarms | CloudWatch alarms are priced based on the resolution of the alarm (e.g. 60 seconds vs 10 seconds) and if you need to combine multiple alarms together into a more complex alarm like anomaly detection or a composite alarm. Pricing is dependant on the region where CloudWatch is deployed.[^3] |
| CloudWatch Logs | AWS charges you for two components as it relates to CloudWatch Logs: (1) ingestion and (2) storage. |
| CloudWatch Events | AWS charges you for CloudWatch Events which are changes in your AWS environment. For example, you can trigger an event whenever an EC2 instance is created. You are charged a rate per one million events. |
| CloudWatch Contributor Insights | Contributor Insights are only available for CloudWatch Logs and DynamoDB. For CloudWatch Logs, Contributor Insights are priced per rule  month, and for every million log events per month that match your rule. For DynamoDB, Contributor Insights are priced per rule per month and for every million DynamoDB Events, which occur when items are read from or written to your DynamoDB table. |
| CloudWatch Canaries | Canaries are priced based on the number of runs. Pricing is very specific to region. Be sure to check where you are running your CloudWatch Canaries to be aware of the price for that region. |

## CloudWatch Cost Optimizations

By default, CloudWatch Log Groups retain logs _indefinitely_. However, you can choose a retention period of anywhere from [one day to 10 years](https://docs.aws.amazon.com/managedservices/latest/userguide/log-customize-retention.html). After logs expire, they will be deleted which will reduce storage costs. To set a retention period, choose `Edit Retention` in the CloudWatch console by following [these instructions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention).

<br />

[^1]: Price is based on US East (Ohio) region as of July 28, 2021. See the footnote below for a comment about pricing per region.

[^2]: Or at least this is what the [CloudWatch pricing page](https://aws.amazon.com/cloudwatch/pricing/) states. If you click through all of the regions the prices are all the same for custom metric storage as of July 28, 2021.

[^3]: Pricing is fairly uniform across regions. Special regions like Sao Paulo and GovCloud diverge from the standard pricing.

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Sep 26, 2021_