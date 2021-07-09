title: S3 Pricing | Vantage Cloud Cost Handbook

[Amazon S3 Pricing Page](https://aws.amazon.com/s3/pricing/)

## Summary

Amazon Simple Storage Service (S3) is an object storage service that allows customers to storage files which are known as "objects". Objects are organized into namespaces named "buckets" for which there is no additional cost for having. Ultimately you are charged on the dimensions below but are a mix of how much you store with specific storage types, the bandwidth for accessing those files and the requests you make to the S3 service. 

## Pricing Dimensions

* **Object Storage Amount**: Amazon S3 charges you for how much you store across all objects across all buckets. There is different pricing rates per region on a per-GB basis and as you store more data on S3, you get discounts on a per-GB basis. 
* **Object Storage Class**: Amazon S3 has many different Storage Classes which are discussed below. "Standard Storage" is the default storage class but you can get discounts for other tiers.
* **Bandwidth**: Amazon S3 charges you for the amount of egress you consume for accessing S3 objects. You should keep an eye on how much bandwidth is being consumed especially if files are left open to the public where you can potentially have runaway costs if signifcant usage occurs. 
* **Request Metrics**: Amazon charges you for GET, SELECT, PUT, COPY, POST and LIST requests. Amazon also charges you different rates depending on which of these request types you're using. This is oftentimes an unknown cost that customers occur that you should keep an eye on. 

## Intelligent Tiering

S3 Intelligent Tiering is an Amazon S3 storage class that automatically will optimize storage costs automatically on behalf of customers. S3 Intelligent Tiering will monitor access patterns of S3 objects on your behalf and shift them between four different storage classes on your behalf to deliver you with savings automatically. 

Typically customers have files that they store with the storage class of Standard Storage but don't think to ever optimize these costs and overpay for the the amount they're storing in S3. By using Intelligent Tiering, customers can focus on their application development and allow S3 Intelligent Tiering to manage shifting their objects' storage classes on their behalf. 

## Understanding Storage Classes

S3 currently supports 19 different object storage types within an S3 Bucket. Each bucket is capable of holding objects from a single class or multiple classes. A light overview of these storage types are below:

* **Standard Storage‍**: Standard Storage (StandardStorage) is for general purpose storage for any type of data, typically used for frequently accessed data. Standard Storage is priced on a tiered basis where it gets incrementally cheaper to store data as you store more. 
* **Intelligent Tiering** - Frequent Access (IntelligentTieringFAStorage)**: Objects uploaded to S3 Intelligent Tiering are automatically stored in the frequent access tier which has the same rates as Standard Storage. 
Intelligent Tiering - Infrequent Access (IntelligentTieringIAStorage): Objects in Frequent Access that haven't been accessed in 30 consecutive days are moved to this tier in which prices drop significantly.
* **Intelligent Tiering - Archive Access (IntelligentTieringAAStorage)**: Upon activating the archive access tier for intelligent tiering, S3 will automatically move objects that haven't been accessed for 90 days to archive access where the pricing is the same as Glacier. 
* **Intelligent Tiering - Deep Archive Access (IntelligentTieringDAAStorage)**: Upon activating the deep archive access tier for intelligent tiering, S3 will automatically move objects that haven't been accessed for 180 days to deep archive access. 
* **S3 Standard - Infrequent Access (StandardIAStorage)**: S3 Standard Infrequent Access is for data that is accessed less frequently, but requires rapid access when needed. It offers the high durability, high throughput, and low latency of S3 Standard, with a low per GB storage price and per GB retrieval fee. This combination of low cost and high performance make S3 Standard-IA ideal for long-term storage, backups, and as a data store for disaster recovery files.
* **Standard Infrequenty Access Overhead (StandardIASizeOverhead)**: There is a minimum billable size of 128KB. For example if you stored an object at 28KB, the StandardIASizeOverhead rate would increase by 128KB-28KB or 100KB and represented by this metric.
* **S3 Standard - Infrequent Access (One Zone)**: S3 Infrequent Access One Zone is for data that is accessed less frequently, but requires rapid access when needed. Unlike other S3 Storage Classes which store data in a minimum of three Availability Zones, S3 Infrequent Access One Zone stores data in a single AZ and costs 20% less than S3 Standard Infrequent Access.
* **One Zone Size Overhead (OneZoneIASizeOverhead)**: There is a minimum billable size of 128KB. For example if you stored an object at 28KB, the StandardIASizeOverhead rate would increase by 128KB-28KB or 100KB and represented by this metric.
* **S3 Glacier (GlacierStorage)**: S3 Glacier is a secure, durable, and low-cost storage class for data archiving. You can reliably store any amount of data at costs that are competitive with or cheaper than on-premises solutions. To keep costs low yet suitable for varying needs, S3 Glacier provides three retrieval options that range from a few minutes to hours.
* **S3 Glacier Overhead (GlacierObjectOverhead)**: For each object that is stored in S3 Glacier, 40 KB of chargeable overhead is added for metadata
* **S3 Glacier Object Overhead (GlacierObjectOverhead)**: Amazon S3 Glacier also requires an additional 32KB of data per object for S3 Glacier’s index and metadata.
* **S3 Glacier Deep Archive (DeepArchiveStorage)**: S3 Glacier Deep Archive is Amazon S3’s lowest-cost storage class and supports long-term retention and digital preservation for data that may be accessed once or twice in a year. It is designed for customers — particularly those in highly-regulated industries, such as the Financial Services, Healthcare, and Public Sectors — that retain data sets for 7-10 years or longer to meet regulatory compliance requirements. S3 Glacier Deep Archive can also be used for backup and disaster recovery use cases, and is a cost-effective and easy-to-manage alternative to magnetic tape systems, whether they are on-premises libraries or off-premises services.
* **Deep Archive Object Overhead (DeepArchiveObjectOverhead)**: For each object that is stored in S3 Glacier, 40 KB of chargeable overhead is added for metadata.
* **Deep Archive S3 Object Overhead (DeepArchiveS3ObjectOverhead)**: Amazon S3 Deep Archive also requires an additional 32KB of data per object for S3 Deep Archive index and metadata.
* **Deep Archive Staging Storage (DeepArchiveStagingStorage)**: Staging storage is where the parts of Multipart Upload are staged until the CompleteMultipart request is issued. The parts are staged in S3 standard, and storage is charged at the S3 Standard price.
* **S3 Reduced Redundancy Storage**: Reduced Redundancy Storage is an Amazon S3 storage option that enables customers to store noncritical, reproducible data at lower levels of redundancy than Amazon S3’s standard storage. It provides a highly available solution for distributing or sharing content that is durably stored elsewhere, or for storing thumbnails, transcoded media, or other processed data that can be easily reproduced. The Reduced Redundancy option stores objects on multiple devices across multiple facilities, providing 400 times the durability of a typical disk drive, but does not replicate objects as many times as standard Amazon S3 storage.


