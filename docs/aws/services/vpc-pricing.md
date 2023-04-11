title: VPC Pricing | Cloud Cost Handbook

[Amazon VPC Pricing Page](https://aws.amazon.com/vpc/pricing/){ .md-button }

## Summary

Amazon Virtual Private Cloud (VPC) is a service which allows customers to logically isolate their resources into different networks. Unless explicitly configured every VPC is completely isolated from every other VPC. There is no charge for a VPC in itself, however some optional sub-components of a VPC can incur charges.

## Pricing Dimensions

|Dimension|Description|
|----|----|
|NAT Gateway Usage|NAT Gateways are billed per hour at a standard rate per region. Each partial hour is billed as a full hour.|
|NAT Gateway Transfer|NAT Gateways are billed per GB which is processed by the gateway regaurdless of where the data is being transferred to or from.|

## NAT Gateway
NAT (Network Address Translation) Gateways enable resources running inside of VPCs to connect to services outside of the VPC without needing to have those resources exposed to the public internet. Besides the standard usage and transfer charges on NAT Gateways you will also be charged standard bandwidth transfer charges on top of that depending on where the traffic is going.

## Amazon VPC Endpoints
VPC Endpoints allow resources to connect to other AWS services outside of a VPC, such as S3, without the need for a NAT Gateway. This is a good way to prevent NAT Gateway usage and transfer charges.

<br/>

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-1szz6puz7-zRuJ8J4OJIiBFlcTobYZXA).