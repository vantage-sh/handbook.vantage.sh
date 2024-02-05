title: WorkSpaces Pricing | Cloud Cost Handbook

[Amazon WorkSpaces Pricing Page](https://aws.amazon.com/workspaces/pricing){ .md-button target="_blank"}

## Summary

Amazon WorkSpaces is a fully managed, persistent desktop virtualization service. You can use Amazon WorkSpaces to provision either Windows or Linux desktops, each with its own set of pricing implications discussed below. WorkSpace pricing can either be done in a monthly or hourly fashion. 

## Pricing Dimensions

|Dimension|Description|
|----|----|
|Compute Type| WorkSpaces offers seven different types of compute types. They are `Value`, `Standard`, `Performance`, `Power`, `PowerPro`, `Graphics`, and `GraphicsPro`. Each of these classes has a different set of underlying resources that contribute to costs differently. The order that these classes are listed in are from cheapest to most expensive. |
|Platform Type| Linux or Windows. You are charged an additional amount of money for running on Windows vs Linux. You may also bring your own license for Windows WorkSpaces to reduce Windows licensing costs if you have that available. |
|Running Mode|`AUTO_STOP` or `ALWAYS_ON`. When you choose `AUTO_STOP` you are choosing to create a WorkSpace that has a pre-determined expiration time in which that WorkSpace will terminate and is billed per hour. When you choose `ALWAYS_ON` you are charged on a monthly rate basis and the WorkSpace will persist being on until you take action to terminate it.  |
|WorkSpace Size| Each compute type offers four different configurations with different amounts of vCPU and GB of Memory. `Graphic` and `GraphicsPro` only offer one size. Depending on the size you choose, you will pay a more expensive rate. |

## Monitoring Unused WorkSpaces

WorkSpaces have an attribute named `last_known_user_connection_timestamp` that maintains a timestamp of the last time a user accessed a specific WorkSpace. You should periodically audit WorkSpaces to ensure that they're being used as otherwise it can be wasteful and a contributor to costs. In the event that this timestamp isn't present, it means that a user has never actually connected to this instance. Additionally, you can look for a certain amount of time that has progressed since a user has accessed it, in the event that a user hasn't accessed a WorkSpace in over a few weeks, it may be a good candidate for a cleanup for cost savings. 

<br />

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Jul 28, 2021_
