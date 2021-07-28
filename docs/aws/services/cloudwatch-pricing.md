title: CloudWatch Pricing | Vantage Cloud Cost Handbook

[Amazon EBS Pricing Page](https://aws.amazon.com/cloudwatch/pricing/){ .md-button }

## Summary

Amazon CloudWatch is a logging, monitoring and observability service. Oftentimes CloudWatch is enabled or leveraged automatically by other AWS services you use and can accrue costs over time for metric and log storage. CloudWatch is an umbrella of different services and as a result, we encourage you to explore subcategory costs of the overall CloudWatch line-item as certain components can accrue costs vs others. 

## Pricing Dimensions

| Dimension | Description |
| -------- | -------- |
| Custom Metric Storage | AWS charges you for the number of custom metrics you store with them per month. |
| CloudWatch API Requests | AWS charges you for the following API requests: `GetMetricData`, `GetInsightRuleReport`, `GetMetricWidgetImage`, `GetMetricStatistics`, `ListMetrics`, `PutMetricData`, `GetDashboard`, `ListDashboards`, `PutDashboard` and `DeleteDashboards`. |
| CloudWatch Dashboards | AWS charges $3.00 per month per CloudWatch dashboard.  |
| CloudWatch Alarms |  |
| CloudWatch Logs | AWS charges you for two components as it relates to CloudWatch Logs: (1) ingestion and (2) storage. |
| CloudWatch Events | AWS charges you for CloudWatch Events which are changes in your AWS environment. For example, you can trigger an event whenever an EC2 instance is created. You are charged a rate per one million events. |
| CloudWatch Contributor Insights |  |
| CloudWatch Canaries |  |

<br />

!!! Contribute
	Help us improve this page by making a contribution on our [Github repository](https://github.com/vantage-sh/handbook).