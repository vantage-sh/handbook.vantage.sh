title: S3 Pricing | Cloud Cost Handbook

[Amazon S3 Pricing Page](https://aws.amazon.com/s3/pricing/){ .md-button }

## Summary

Amazon Simple Storage Service (S3) is an object storage service that allows customers to store files called *objects*. Objects are organized into namespaces called *buckets* at no additional cost. Ultimately, you are charged on the dimensions below, which are a mix of how much you store with specific storage types, the bandwidth for accessing those files, and the requests you make to the S3 service. 

## Pricing Dimensions

|Dimension|Description|
|----|----|
|Object Storage Amount|AWS charges you for how much you store across all objects and across all buckets. Each region has a different pricing rate on a per-GB basis, and as you store more data on S3, you get discounts on a per-GB basis.| 
|Object Storage Class|Amazon S3 has many different storage classes, further discussed below. S3 Standard is the default storage class, but you can get discounts for other tiers.|
|Bandwidth|AWS charges you for the amount of egress you consume for accessing S3 objects. You should keep an eye on how much bandwidth is being consumed—, where you can potentially have runaway costs with significant use.| 
|Request Metrics|AWS charges you for GET, SELECT, PUT, COPY, POST, and LIST requests. S3 also charges you different rates depending on which of these request types you're using. This is oftentimes an unknown cost that occurs and that you should keep an eye on.| 

## Intelligent-Tiering

S3 Intelligent-Tiering is an Amazon S3 storage class that will automatically optimize storage costs on your behalf. S3 Intelligent-Tiering will monitor access patterns of S3 objects and shift them between four different storage classes to deliver you with automatic savings. 

Typically, customers have files stored in S3 Standard storage, but they may not think to ever optimize these costs and overpay for the number of files they're storing in S3. By using Intelligent-Tiering, you can focus on your application development and allow S3 Intelligent-Tiering to manage shifting their objects' storage classes on their behalf. 

## Understanding Storage Classes

S3 currently supports 19 different object storage types within an S3 bucket. Each bucket is capable of holding objects from a single class or multiple classes. A light overview of these storage types is included below:

|Storage Type|Description|
|----|----|
|Standard Storage‍|Standard Storage (StandardStorage) is for general purpose storage for any type of data, typically used for frequently accessed data. Standard Storage is priced on a tiered basis, where it gets incrementally cheaper to store data as you store more.| 
|Express One Zone|This storage class is a high-performance storage class that is built to provide consistent single-digit millisecond data access. It provides 10 times faster access than S3 Standard; however, the storage pricing is a lot higher—at almost 7 times the rate of Standard storage pricing. Request pricing is charged at a flat rate that's half the rate of Standard pricing, for request sizes up to 512KB. Additional per-GB charges apply for request sizes greater than 512KB  |
|Intelligent Tiering - Frequent Access (IntelligentTieringFAStorage)|Objects uploaded to S3 Intelligent Tiering are automatically stored in the frequent access tier which has the same rates as Standard Storage.| 
|Intelligent-Tiering - Infrequent Access (IntelligentTieringIAStorage)| Objects in Frequent Access that haven't been accessed in 30 consecutive days are moved to this tier, where prices drop significantly.|
|Intelligent-Tiering - Archive Access (IntelligentTieringAAStorage)|Upon activating the archive access tier for intelligent tiering, S3 will automatically move objects that haven't been accessed for 90 days to archive access, where the pricing is the same as Glacier.| 
|Intelligent Tiering - Deep Archive Access (IntelligentTieringDAAStorage)|Upon activating the deep archive access tier for Intelligent-Tiering, S3 will automatically move objects that haven't been accessed for 180 days to deep archive access.| 
|S3 Standard - Infrequent Access (StandardIAStorage)|S3 Standard Infrequent Access is for data that is accessed less frequently, but requires rapid access when needed. It offers the high durability, high throughput, and low latency of S3 Standard, with a low per-GB storage price and per-GB retrieval fee. This combination of low cost and high performance make S3 Standard-IA ideal for long-term storage, backups, and as a data store for disaster recovery files.|
|Standard Infrequently Access Overhead (StandardIASizeOverhead)|There is a minimum billable size of 128KB. , if you stored an object at 28KB, the StandardIASizeOverhead rate would increase by 128KB–28KB or 100KB and represented by this metric.|
|S3 Standard - Infrequent Access (One Zone)|S3 Infrequent Access One Zone is for data that is accessed less frequently, but requires rapid access when needed. Unlike other S3 Storage classes that store data in a minimum of three Availability Zones, S3 Infrequent Access One Zone stores data in a single AZ and costs 20% less than S3 Standard Infrequent Access.|
|One Zone Size Overhead (OneZoneIASizeOverhead)|There is a minimum billable size of 128KB. For example, if you stored an object at 28KB, the StandardIASizeOverhead rate would increase by 128KB–28KB or 100KB and represented by this metric.|
|S3 Glacier (GlacierStorage)|S3 Glacier is a secure, durable, and low-cost storage class for data archiving. You can reliably store any amount of data at costs that are competitive with or cheaper than on-premises solutions. To keep costs low yet suitable for varying needs, S3 Glacier provides three retrieval options that range from a few minutes to hours.|
|S3 Glacier Overhead (GlacierObjectOverhead)|For each object that is stored in S3 Glacier, 40 KB of chargeable overhead is added for metadata|
|S3 Glacier Object Overhead (GlacierObjectOverhead)|Amazon S3 Glacier also requires an additional 32KB of data per object for S3 Glacier’s index and metadata.|
|S3 Glacier Deep Archive (DeepArchiveStorage)|S3 Glacier Deep Archive is Amazon S3’s lowest-cost storage class and supports long-term retention and digital preservation for data that may be accessed once or twice in a year. It is designed for customers—particularly those in highly-regulated industries, such as the Financial Services, Healthcare, and Public Sectors–that retain data sets for 7–10 years or longer to meet regulatory compliance requirements. S3 Glacier Deep Archive can also be used for backup and disaster recovery use cases, and is a cost-effective and easy-to-manage alternative to magnetic tape systems, whether they are on-premises libraries or off-premises services.|
|Deep Archive Object Overhead (DeepArchiveObjectOverhead)|For each object that is stored in S3 Glacier, 40 KB of chargeable overhead is added for metadata.|
|Deep Archive S3 Object Overhead (DeepArchiveS3ObjectOverhead)|Amazon S3 Deep Archive also requires an additional 32KB of data per object for S3 Deep Archive index and metadata.|
|Deep Archive Staging Storage (DeepArchiveStagingStorage)|Staging storage is where the parts of Multipart Upload are staged until the CompleteMultipart request is issued. The parts are staged in S3 Standard, and storage is charged at the S3 Standard price.|
|S3 Reduced Redundancy Storage|Reduced Redundancy Storage is an Amazon S3 storage option that enables customers to store noncritical, reproducible data at lower levels of redundancy than Amazon S3 Standard storage. It provides a highly available solution for distributing or sharing content that is durably stored elsewhere, or for storing thumbnails, transcoded media, or other processed data that can be easily reproduced. The Reduced Redundancy option stores objects on multiple devices across multiple facilities, providing 400 times the durability of a typical disk drive, but does not replicate objects as many times as standard Amazon S3 storage.|


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


## S3 Versus Cloudflare Bandwidth Alliance Partner

The [Cloudflare Bandwidth Alliance](https://www.cloudflare.com/bandwidth-alliance/) is a group of infrastructure providers that have decided to either completely waive or massively discount egress fees for shared customers. This can be a huge source of savings for customers that have an AWS bill where S3 egress costs make up a large portion of the aforementioned bill.

By moving S3 content to Cloudflare's content delivery network (CDN) service in tandem with a Bandwidth Alliance provider, you can get no-cost content transit from their Cloudflare origin server to Cloudflare servers distributed around the world. This effectively reproduces the cost benefit that users get for pairing CloudFront with an AWS service, like S3.[^noegressfees] Utilizing one of Cloudflare's self-serve plans, you can also cap their cost to deliver content via flat-rate pricing. Further details can be found at in the [CloudFront service article](https://handbook.vantage.sh/aws/services/cloudfront-pricing/#cloudfront-versus-cloudflare) of the Cloud Cost Handbook.

### Considerations

Price is not the only consideration that goes into making a decision about whether to utilize S3 or a competing storage service. Performance, availability, user experience, support, and legal compliance are other factors that will factor into the decision to utilize one service over another.

#### Complexity

AWS had made it exceedingly easy for customers to utilize other AWS services in tandem, but there is a non-trivial cost for an organization to decide to split their infrastructure over multiple service providers. Developers will need to learn and understand both systems and when to choose one design pattern over the other. There will be two sets of documentation that will need to be addressed when designing or troubleshooting systems.

#### Use-cases

The primary use-case in favor of utilizing this cost efficiency architecture strategy is if a user has a large amount of static content that is stored on S3 and being served to end-users via the internet.

[^noegressfees]: "If you are using an AWS origin, effective December 1, 2014, data transferred from origin to edge locations (Amazon CloudFront "origin fetches") will be free of charge." https://aws.amazon.com/cloudfront/pricing/


<br/>

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).
