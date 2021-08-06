title: Cloudfront Pricing | Cloud Cost Handbook

[Amazon CloudFront Pricing Page](https://aws.amazon.com/cloudfront/pricing/){ .md-button }

## Summary

Amazon CloudFront is a content delivery network (CDN) service used to distribute and cache traffic from one region to multiple geographic endpoints globally. Every CloudFront distribution includes an origin which is used to pull the original data from. An origin will typically be an S3 bucket or Load Balancer Endpoint. The traffic is distributed globally to speed up the access to an application which recieves visitors from across the globe. CloudFront Distributions are billed based on the amount of traffic they request from the origin, distribute out to the internet as well as per request processed. Distribution out to the internet is priced differently depending on the region which it is accessed. Regions are grouped into geographic regions. When creating a distribution it is possible to select which regions CloudFront will serve traffic from.

## Pricing Dimensions

| Dimension | Description |
| -- | -- |
| Transfer Out to Internet | Distributions are billed per GB of data transfered out of a geographic area to the internet. The prices are tiered and are lower the more traffic is transferred. |
| Regional Data Transfer Out to Origin | Distributions are billed per GB of data transfer from the distribution back to the origin. The prices are a flat-rate and dependent on their geographic area. |
| Per Request | Distributions are billed per 10,000 requests and are different rates based on whether the request is HTTP or HTTPS. If origin shield is configured there is an additional charge per 10,000 requests and are a standard rate regardless of protocol. Both are priced differently depending on geographic area. |

## Origin Shield

Origin Shield can be enabled in order to reduce the amount of traffic being served directly from the origin. Origin shields are not available in every region.

## Custom Pricing

For customers who are willing to make certain minimum traffic commits (typically 10 TB/month or higher) they can contact AWS and negotiate custom discounted rates.


## CloudFront Versus Cloudflare

Cloudflare[^whynoothervendors] is an edge network that offers a number of different performance, availability and security services. One of those services is an edge caching service that offer effectively the same service as Amazon CloudFront. The most important distinction between CloudFront and Cloudflare is not a technical differentiation but a business model differentiation. CloudFront utilizes a metered pricing model whereby you pay based on the amount of traffic that is served via the CloudFront service.[^cloudfrontpricing] Cloudflare, on the otherhand, offers flat-rate pricing for its service without any bandwidth caps.[^cloudflaretos] 

What this means is that as a customer of [Cloudflare's Business plan](https://www.cloudflare.com/plans/business/), you can pay $200 per month and delivery unlimited traffic via the Cloudflare CDN. Seems too good to be true? Feel free to browse the official Cloudflare community where this question is [asked](https://community.cloudflare.com/t/to-support-about-cdn-plan/166219) and [answered](https://community.cloudflare.com/t/cloudflare-doesnt-mention-in-plans-that-how-much-monthly-bandwidth-will-provides/161097) multiple times.

### Considerations

Price is not the only consideration that goes into making a decision about whether to utilize CloudFront or a competing CDN service. Performance, availability, user experience, support and legal compliance are other factors that will factor into the decision to utilize one service over another.

#### Availability

In order to offer customers unlimited bandwidth, Cloudflare utilizes service degradation based on their plan levels to prioritize higher tier customers in the event of a service degredation. The two most common service degradations for Cloudflare are either a DDoS attack that is overwhelming one or more points-of-presence (PoP) in the network or a legitimate surge in traffic due to any number of events. 

When the resources for a PoP are being depleted and service is being degraded, Cloudflare will choose to route traffic for customers out of that location based on the plan level they are subscribed to. Free traffic will be routed away from the PoP first, then Pro, Business, etc. The effect of having traffic routed out of a specific PoP is that users that are closest to the PoP will have some level of service degredation since they will instead have their traffic served from a PoP that is farther away than their most ideal PoP. In locations where the next nearest available PoP is close this degredation will be practically unnoticable. In locations where the next available PoP is topologically distant service degredation can potentially be significant.

#### Technical

In the scenario that you are utilizing CloudFront and have an Amazon service designated as the origin for the content being served, typically this would be an S3 bucket or maybe EC2 with an attached EBS volume, you should consider that by switch from CloudFront as your CDN to Cloudflare you will incur egress charges for data transfer from AWS to Cloudflare. AWS does not charge customers any egress fees when moving content from an AWS service like S3 or EC2 to CloudFront.[^freeoriginegress] The amount of charges will largely be dependent on your particular services cache hit ratio. The higher the cache hit ratio, the less cache misses that will incur AWS egress charges.

This practice favors pairing CloudFront with an AWS service as origin. That being said, for most customers with significant  CloudFront traffic they will still come out on top by considering a flat-rate priced CDN plan.

On top of this, you can also consider moving your content off of an AWS service to a provider in the [Bandwidth Alliance](https://www.cloudflare.com/bandwidth-alliance/). By utilizing the Cloudflare CDN service and a Bandwidth Alliance partner as the content origin, you can take advantage of the flat-rate pricing of the Cloudflare self-serve plans and eliminate all egress costs between Cloudflare and your origin provider of choice. This effectively gives you the same benefit that AWS offers customer of no egress charges between an AWS service and CloudFront but with the power of the flat-rate pricing that is available via the Cloudflare self-serve plans. Further details can be found at in the [S3 service article](https://handbook.vantage.sh/aws/services/s3-pricing/#s3-versus-bandwidth-alliance-partner) of the Cloud Cost Handbook.

<!--- Add section here explaining considerations around usage of a single domain over multiple domains -->

#### Sales

Another side effect of subscribing to a self-serve plan from Cloudflare is that users of these plans are used as part of the sales funnel for the Cloudflare sales team. What this means is that by signing up for Cloudflare you are giving your contact information that can be utilized by the sales team in order for them to contact you about other Cloudflare services and offerings. 

The important thing to remember is that, as long as you aren't breaking the Cloudflare Terms of Service (ToS) they cannot force you to purchase any additional services.


[^whynoothervendors]: This guide is calling special attention to Cloudflare and no other vendors in this space due to the unique offerings that Cloudflare has that no other provider offers. Specifically, that they offer self-serve plans with flat-rate pricing and no bandwidth caps. If you are aware of any other services with a similar offering, please submit an issue or pull request and we will update the guide.

[^cloudfrontpricing]: Direct link to CloudFront pricing that details metered pricing model: https://aws.amazon.com/cloudfront/pricing/

[^cloudflaretos]: Direct link to the Cloudflare Terms of Service for the self-serve plans (i.e. the Free, Pro and Business plans):https://www.cloudflare.com/terms/

[^freeoriginegress]: "If you are using an AWS origin, effective December 1, 2014, data transferred from origin to edge locations (Amazon CloudFront "origin fetches") will be free of charge." https://aws.amazon.com/cloudfront/pricing/

<br/>

!!! Contribute
	Help us improve this page by making a contribution on our [Github repository](https://github.com/vantage-sh/handbook).