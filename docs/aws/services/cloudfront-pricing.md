title: Cloudfront Pricing | Vantage Cloud Cost Handbook

[Amazon CloudFront Pricing Page](https://aws.amazon.com/cloudfront/pricing/)

## Summary
Amazon CloudFront is a CDN service used to distribute and cache traffic from one region to multiple geographic endpoints globally. Every CloudFront distribution includes an origin which is used to pull the original data from. An origin will typically be an S3 bucket or Load Balancer Endpoint. The traffic is distributed globally to speed up the access to an application which recieves visitors from across the globe. CloudFront Distributions are billed based on the amount of traffic they request from the origin, distribute out to the internet as well as per request processed. Distribution out to the internet is priced differently depending on the region which it is accessed. Regions are grouped into geographic regions. When creating a distribution it is possible to select which regions CloudFront will serve traffic from.

## Pricing Dimensions

* **Transfer Out to Internet**: Distributions are billed per GB of data transfered out of a geographic area to the internet. The prices are tiered and are lower the more traffic is transferred.

* **Regional Data Transfer Out to Origin**: Distributions are billed per GB of data transfer from the distribution back to the origin. The prices are a flat rate and dependent on their geographic area.

* **Per Request**: Distributions are billed per 10,000 requests and are different rates based on whether the request is HTTP or HTTPS. If origin shield is configured there is an additional charge per 10,000 requests and are a standard rate regardless of protocol. Both are priced differently depending on geographic area. 

## Origin Shield
Origin Shield can be enabled in order to reduce the amount of traffic being served directly from the origin. Origin shields are not available in every region.

## Custom Pricing
For customers who are willing to make certain minimum traffic commits (typically 10 TB/month or higher) they can contact AWS and negotiate custom discounted rates.
