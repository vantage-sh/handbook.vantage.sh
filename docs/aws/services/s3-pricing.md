title: S3 Pricing | Cloud Cost Handbook

[Amazon S3 Pricing Page](https://aws.amazon.com/s3/pricing/){ .md-button target="_blank"}

## Summary

Amazon Simple Storage Service (S3) is an object storage service that allows customers to store files called objects. Objects are organized into namespaces called buckets at no additional cost. Ultimately, you are charged on the dimensions below, which are a mix of how much you store with specific storage types, the bandwidth for accessing those files, and the requests you make to the S3 service. 

## Pricing Dimensions

|Dimension|Description|
|----|----|
|Object Storage Amount|AWS charges you for how much you store across all objects and across all buckets. Each region has a different pricing rate on a per GB basis, and as you store more data on S3, you may get discounts on a per GB basis.| 
|Object Storage Class|Amazon S3 has many different storage classes, further discussed below. Standard is the default storage class, but you can get lower rates for some other tiers.|
|Bandwidth|AWS charges you for the amount of egress you consume for accessing S3 objects. You should keep an eye on how much bandwidth is being consumed—that's where you can potentially have runaway costs with significant use.| 
|Request Metrics|AWS charges you for `GET`, `SELECT`, `PUT`, `COPY`, `POST`, and `LIST` requests. S3 also charges you different rates depending on which of these request types you're using. This is oftentimes an unknown cost that occurs and that you should keep an eye on.| 

## Intelligent-Tiering

S3 Intelligent-Tiering is an Amazon S3 storage class that will automatically optimize storage costs on your behalf. S3 Intelligent-Tiering will monitor access patterns of S3 objects and shift them between five different storage classes to deliver you automatic savings. 

Typically, customers have files stored in S3 Standard storage, but they may not think to ever optimize these costs and overpay for the number of files they're storing in S3. By using Intelligent-Tiering, you can focus on your application development and allow S3 Intelligent-Tiering to manage shifting their objects' storage classes on your behalf. 

## Understanding Storage Classes

S3 currently supports 28 different object storage types within an S3 bucket. Each bucket is capable of holding objects from a single class or multiple classes. A light overview of these storage types is included below:

| Storage Type | Description |
| --- | --- |
| Standard Storage (StandardStorage) | Standard Storage is for general purpose storage of any type of data, typically used for frequently accessed data. Standard Storage is priced on a tiered basis where it gets incrementally cheaper to store data as you store more. |
| Intelligent-Tiering - Frequent Access (IntelligentTieringFAStorage) | Objects uploaded to Intelligent-Tiering are automatically stored in the Frequent Access tier which has the same rates as Standard Storage. |
| Intelligent-Tiering - Infrequent Access (IntelligentTieringIAStorage) | Objects in Frequent Access that haven't been accessed in 30 consecutive days are moved to this tier in which prices drop significantly. |
| Intelligent-Tiering - Archive Instant Access (IntelligentTieringAIAStorage) | Objects that haven’t been accessed in 90 consecutive days are moved to this tier in which prices drop even more. |
| Intelligent-Tiering - Archive Access (IntelligentTieringAAStorage) | Upon activating the Archive Access tier for Intelligent-Tiering, S3 will automatically move objects that haven’t been accessed for 90 days (or more depending on your configuration) to Archive Access where the pricing is the same as Glacier. |
| Intelligent-Tiering - Deep Archive Access (IntelligentTieringDAAStorage) | Upon activating the Deep Archive Access tier for Intelligent-Tiering, S3 will automatically move objects that haven’t been accessed for 180 days (or more depending on your configuration) to Deep Archive Access. |
| Intelligent-Tiering - Archive Access Object Overhead (IntAAObjectOverhead) | For each object that is stored in the Intelligent-Tiering - Archive Access tier, 32KB of chargeable overhead is added for index and related metadata, charged at Glacier Flexible Retrieval rates. |
| Intelligent-Tiering - Archive Access S3 Object Overhead (IntAAS3ObjectOverhead) | Intelligent-Tiering - Archive Access also requires an additional 8KB of data per object for the name of the object and other metadata, charged at Standard Storage rates |
| Intelligent-Tiering - Deep Archive Access Object Overhead (IntDAAObjectOverhead) | For each object that is stored in the Intelligent-Tiering - Deep Archive Access tier, 32KB of chargeable overhead is added for index and related metadata, charged at Glacier Flexible Retrieval rates. |
| Intelligent-Tiering - Deep Archive Access S3 Object Overhead (IntDAAS3ObjectOverhead) | Intelligent-Tiering - Deep Archive Access also requires an additional 8KB of data per object for the name of the object and other metadata, charged at Standard Storage rates. |
| Standard - Infrequent Access (StandardIAStorage) | Standard - Infrequent Access is for data that is accessed less frequently but requires rapid access when needed. It offers the high durability, high throughput, and low latency of Standard Storage, with a low per GB storage price and per GB retrieval fee. This combination of low cost and high performance makes Standard - Infrequent Access ideal for long-term storage, backups, and as a data store for disaster recovery files. |
| Standard - Infrequent Access Size Overhead (StandardIASizeOverhead) | There is a minimum billable object size of 128KB. For example, if you stored an object at 28KB, the rate would increase by 100KB, (128KB - 28KB) and is represented by this metric. |
| Standard - Infrequent Access Object Overhead (StandardIAObjectOverhead) | For each object stored in Standard - Infrequent Access 32KB of chargeable overhead is added for metadata. |
| Standard - Infrequent Access (One Zone) (OneZoneIAStorage) | Standard - Infrequent Access (One Zone) is for data that is accessed less frequently but requires rapid access when needed. Unlike other S3 storage classes which store data in a minimum of three Availability Zones (AZ), Standard - Infrequent Access (One Zone) stores data in a single AZ and costs much less than Standard - Infrequent Access. |
| One Zone Size Overhead (OneZoneIASizeOverhead) | There is a minimum billable object size of 128KB. For example, if you stored an object at 28KB, the rate would increase by 100KB, (128KB - 28KB) and is represented by this metric. |
| Glacier Instant Retrieval (GlacierInstantRetrievalStorage) | Glacier Instant Retrieval (GlacierInstantRetrievalStorage) is a high-latency, low-cost, durable archive storage class. The use case is ideal for data that requires long-term storage and is only accessed once per quarter. |
| Glacier Instant Retrieval Size Overhead (GlacierInstantRetrievalSizeOverhead) | There is a minimum billable object size of 128KB. For example, if you stored an object at 28KB, the rate would increase by 100KB, (128KB - 28KB) and is represented by this metric. |
| Glacier Flexible Retrieval (GlacierStorage) | Glacier Flexible Retrieval (formerly called Glacier) is a secure, durable, and low-cost storage class for data archiving. You can reliably store any amount of data at costs that are competitive with or cheaper than on-premises solutions. To keep costs low yet suitable for varying needs, Glacier provides three retrieval options that range from a few minutes to hours.  |
| Glacier Overhead (GlacierObjectOverhead) | For each object that is stored in Glacier, 32KB of chargeable overhead is added for index and related metadata, charged at Glacier Flexible Retrieval rates. |
| Glacier S3 Object Overhead (GlacierS3ObjectOverhead) | Glacier also requires an additional 8KB of data per object for the name of the object and other metadata, charged at Standard Storage rates. |
| Glacier Staging Storage (GlacierStagingStorage) | Staging storage serves as the temporary holding space for the components of a Multipart Upload until the CompleteMultipart request is initiated. These parts are temporarily stored in Standard Storage, and chargers based on Standard Storage pricing. |
| Glacier Deep Archive (DeepArchiveStorage) | Glacier Deep Archive (DeepArchiveStorage) is tied with Intelligent-Tiering - Deep Archive Access as Amazon S3’s lowest-cost storage class. It supports long-term retention and digital preservation of data that may be accessed once or twice a year. It is designed for customers‚ particularly those in highly-regulated industries, such as the Financial Services, Healthcare, and Public Sectors, that retain data sets for 7-10 years or longer to meet regulatory compliance requirements. Glacier Deep Archive can also be used for backup and disaster recovery use cases, and is a cost-effective and easy-to-manage alternative to magnetic tape systems, whether they are on-premises libraries or off-premises services. |
| Deep Archive Object Overhead (DeepArchiveObjectOverhead) | For each object that is stored in Glacier Deep Archive, 32KB of chargeable overhead is added for index and related metadata, charged at Glacier Deep Archive rates. |
| Deep Archive S3 Object Overhead (DeepArchiveS3ObjectOverhead) | Glacier Deep Archive also requires an additional 8KB of data per object for the name of the object and other metadata, charged at Standard Storage rates. |
| Deep Archive Staging Storage (DeepArchiveStagingStorage) | Staging storage is where the parts of Multipart Upload are staged until the CompleteMultipart request is issued. The parts are staged in Standard Storage, and storage is charged at the Standard Storage price. |
| S3 Reduced Redundancy Storage | is an Amazon S3 storage option that enables customers to store noncritical, reproducible data at lower levels of redundancy than Standard Storage. It provides a highly available solution for distributing or sharing content that is durably stored elsewhere, or for storing thumbnails, transcoded media, or other processed data that can be easily reproduced. The Reduced Redundancy Storage option stores objects on multiple devices across multiple facilities, providing 400 times the durability of a typical disk drive, but does not replicate objects as many times as Standard Storage. |
| Express One Zone (ExpressOneZone) | Express One Zone, like Standard - Infrequent Access (One Zone) is a single AZ storage class. It can provide extremely quick, single-digit millisecond access to your data at a lower price than Standard Storage. Some examples of use cases are Machine Learning and Financial Modeling.  |
| Outposts (Outposts) | AWS Outposts extend AWS services, tools, etc to your on-premises AWS Outposts environment. Ideal for locally required data, with S3 on Outposts you can reliably store and access data on your Outpost. |

## S3 Bucket Request Metrics

S3 does not have ingress, egress, or request metrics turned on by default, leaving many users unsure of what their costs will be until they receive their monthly AWS bill. That being said, it's relatively easy to enable these metrics. 

Below is an example of how to enable these metrics for a S3 bucket via the AWS CLI. Just be sure to replace `YOUR_BUCKET_NAME` with your actual bucket name and `YOUR_BUCKET_REGION` with the appropriate bucket region.

```
aws s3api put-bucket-metrics-configuration 
  --bucket YOUR_BUCKET_NAME
  --metrics-configuration Id=EntireBucket 
  --id EntireBucket 
  --region YOUR_BUCKET_REGION
```

!!! Note 
    It takes roughly 15 minutes for AWS to begin delivering these metrics after being enabled.

## S3 Vs Cloudflare Bandwidth Alliance Partner

The [Cloudflare Bandwidth Alliance](https://www.cloudflare.com/bandwidth-alliance/) is a group of infrastructure providers that have decided to either completely waive or massively discount egress fees for shared customers. This can be a huge source of savings for customers who have an AWS bill where S3 egress costs make up a large portion of the aforementioned bill.

By moving S3 content to Cloudflare's content delivery network (CDN) service in tandem with a Bandwidth Alliance provider, you can get no-cost content transit from their Cloudflare origin server to Cloudflare servers distributed around the world. This effectively reproduces the cost benefit that users get for pairing CloudFront with an AWS service, like S3.[^noegressfees] Utilizing one of Cloudflare's self-serve plans, you can also cap their cost to deliver content via flat-rate pricing. Further details can be found in the [CloudFront section](/aws/services/cloudfront-pricing/) of the Cloud Cost Handbook.

### Considerations

Price is not the only consideration that goes into making a decision about whether to utilize S3 or a competing storage service. Performance, availability, user experience, support, and legal compliance are other factors that will factor into the decision to utilize one service over another.

#### Complexity

AWS has made it exceedingly easy for customers to utilize other AWS services in tandem, but there is a non-trivial cost for an organization to decide to split their infrastructure over multiple service providers. Developers will need to learn and understand both systems and when to choose one design pattern over the other. There will be two sets of documentation that will need to be addressed when designing or troubleshooting systems.

#### Use Cases

The primary use case in favor of utilizing this cost-efficiency architecture strategy is if a user has a large amount of static content that is stored on S3 and being served to end-users via the internet.

[^noegressfees]: "If you are using an AWS origin, effective December 1, 2014, data transferred from origin to edge locations (Amazon CloudFront origin fetches) will be free of charge." https://aws.amazon.com/cloudfront/pricing/

<br/>

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Feb 2, 2024_
