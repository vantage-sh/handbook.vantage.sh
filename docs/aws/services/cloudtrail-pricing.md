title: CloudTrail Pricing | Cloud Cost Handbook

[AWS CloudTrail Pricing Page](https://aws.amazon.com/cloudtrail/pricing/){ .md-button target="_blank"}

## Summary

AWS CloudTrail maintains logs and records of actions and events that occur in your AWS account. It records actions like user and resource activity, API calls, and configuration changes. These logs are useful for troubleshooting operational issues as well as investigating potential security incidents. 


## Pricing Dimensions

| Dimension  | Description |
| ------------- |-------------|
|Ingestion and storage| For CloudTrail Lakes, you pay for both ingesting and storing of logs/events from AWS sources and non-AWS sources. Pricing does not differ between source. This pricing includes 7 years of storage. |
|Analysis| Analysis charges for CloudTrail Lakes are based on the volume of logs you analyze. You are charged per GB of scanned data. CloudTrail Insights analysis charges are based on the Insight type.|
| Events delivered| For CloudTrail Trails, pricing is based on the number of data events and management events delivered to S3. Your first management event delivery to S3 is free. |

## Event History 

Use the event history feature directly in the CloudTrail console to view and search historical event and log data. The event history captures only management events (for example, if you create or delete S3 buckets). The event history does not include data events (for example, if you read or write an S3 object). Event history shows only a 90-day history of the account's activity. You can query across only one [Region](/aws/concepts/regions/){target="_blank"} and a single attribute. Event history has no additional charge. 


## CloudTrail Trails

Trails collect and store AWS account activity. Trails support the delivery of both management and data events. Unlike the basic event history, Trails contain an event record history that can be greater than 90 days. Additionally, you can specify where to send this activity to in S3 buckets, CloudWatch Logs, or Amazon EventBridge. You have the option to [set up Amazon SNS notifications](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html){target="_blank"} to alert you when CloudTrail adds a new log file to an S3 bucket.  


## CloudTrail Lake

A CloudTrail Lake allows you to store and analyze API activity and data logs for up to 7 years. You have the ability to view log data from multiple sources and query on numerous records. Compared to the event history, you can create more customized views and run queries for multiple Regions and attributes. You pay for both ingestion and storage based on "uncompressed data ingested during the month." AWS offers [a few suggestions for reducing usage costs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html#cloudtrail-lake-manage-costs-tools){target="_blank"}, including configuring your options to not ingest future events. 


## CloudTrail Insights

CloudTrail Insights analyzes management events and reports on unusual or suspicious activity. Events are logged when Insights notices actions that differ from your account's usual event pattern. For example, if Insights starts to see a large increase in deletion API calls, an event is generated. Pricing is based on every 100,000 events analyzed per each Insight type.  

<br/>

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).
