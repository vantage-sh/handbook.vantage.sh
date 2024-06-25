title: VPC Flow Logs Pricing | Cloud Cost Handbook

[Amazon VPC Flow Logs Pricing Page](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-pricing.html){ .md-button target="\_blank"}

## Summary

VPC Flow Logs is an AWS feature that records inbound and outbound IP traffic information from your Virtual Private Cloud (VPC). Flow logs can be used for many uses cases, including:

- Monitor network traffic patterns between source and destination.
- Review traffic flows for compliance requirements and security reviews.
- Monitor for performance and potential bottlenecks. You can review for bytes and packets transferred, latency, and protocol distribution (e.g., percentage of traffic using TCP, UDP, etc.) and packet loss.

VPC Flow Logs capture metadata about the traffic flow, such as protocol, bytes, action (e.g., accept/reject), type of traffic (e.g., IPv4, IPv6), ports, packets transferred, and more.

Logs can be stored in the following locations:

- Amazon CloudWatch Logs
- Amazon S3
- Amazon Data Firehose

## VPC Flow Logs Considerations

Consider the following options when you create flow logs:

- **Data Volume**: Once you enable flow logs, the traffic can generate large volumes of data, leading to high costs. When creating flow logs, you can filter on whether you want to log accepted, rejected, or all traffic.
- **Custom or Default Format**: The _default format_ includes a set of predefined fields. If you want to define different fields or order of fields, select a _custom format_ for logs.
- **File Format:** When you create a flow log, you have the option to specify either text (default) or Parquet file formats. Parquet compressed with Gzip takes up 20% less strorage—and therefore less storage costs—than Gzip text format.
- **Aggregation Interval**: When you create a flow log, you can add the aggregation interval, which is the timeframe for which the traffic flow is analyzed and recorded into a flow log. According to AWS, once this data is captured, “The flow log service typically delivers logs to CloudWatch Logs in about 5 minutes and to Amazon S3 in about 10 minutes.”
- **Storage Location:** Consider aggregating all logs and storing them in a single S3 bucket to reduce costs. Consider options for long-term storage, like Glacier storage classes, which can help you save on costs.

After you create flow logs, consider the following points:

- **Permissions**: Ensure that the IAM roles and permissions are correctly set up to allow VPC Flow Logs to write to CloudWatch Logs, S3, or Kinesis. Incorrect permissions might result in log delivery failures.
- **Latency and Delivery Time**: When you first create a flow log, it can take some time for data to start being published to the chosen destination. These logs are not sent in real time. There also might be a delay between when traffic occurs and when flow logs are available for analysis.
- **Unlogged Traffic**: Not all network traffic is logged. For example, traffic that flows between an endpoint network interface and a Network Load Balancer network interface is not logged. DHCP traffic and mirrored traffic are also not logged.
- **Cost Allocation Tagging:** Consider using tags to identify metadata or owners for logs and costs. This can help with determining which teams are responsible for costly logs. See the [AWS documentation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) for details.

## VPC Flow Logs Pricing Dimensions

With regard to pricing, VPC Flow Logs fall into the category of [Vended logs](https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs). Vended logs are “logs natively published by AWS services on behalf of the customer and available at volume discount pricing.” Pricing is mostly based on the amount of data captured. The full cost is determined by the volume of log data and the destination for storage (i.e., CloudWatch Logs, S3, or Data Firehose).

| Dimension       | Description                                                                                                                                                                                                                                                                            |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Ingestion  | Pricing varies based on ingestion location—CloudWatch Logs, S3, and Data Firehose. For CloudWatch Logs, there are Standard and Infrequent Access options. Charges are based on the amount of data ingested. Per GB charges decrease as the amount of data ingested increases. |
| Storage Charges | The cost of storing the log data. For CloudWatch Logs, you’re charged per GB per month. For S3, charges are per GB per month for data stored, with different rates for Standard and Glacier storage classes.                                                                            |

<br/>

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Jun 14, 2024_
