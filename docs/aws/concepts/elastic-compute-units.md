title: ECU Pricing | Cloud Cost Handbook

## vCPUs and Real CPUs


## Elastic Compute Unit Considerations

* **Target Scaling** adds or removes capacity to keep a metric as near a specific value as possible. For example, target average CPU utilization of 50% across a set of ECS Tasks. If CPU utilization gets too high, add nodes. If CPU utilization gets too low, remove nodes.
* **Step Scaling** will adjust capacity up and down by dynamic amounts, depending on the magnitude of a metric.
* **Scheduled Scaling** will adjust mininmum and maximum capacity settings on a schedule.
* **Simple Scaling** will add or remove EC2 instances from an Autoscalng Group when an alarm is in alert state.
* **Predictive Scaling** can leverage historical metrics to preemptively scale EC2 workloads based on daily or weekly trends.
* **Manual Scaling** is possible with EC2 instances if teams need to intervene with an autoscaling group. This allows you to manually adjust the autoscaling target without any automation. 

## Other Considerations


!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-oey52myv-gq4AWRKkX25kjp1UGziPTw).

