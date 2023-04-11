title: Rightsizing 

Rightsizing is a term used for identifying and augmenting certain resources for greater utilization and potential cost savings. Typically rightsizing occures when you're over-provisioned and can apply to a variety of services with some examples below:

* **EC2 Instances**: Oftentimes customers will choose one EC2 Instance that is over-allocated in terms the amount of vCPU and GB of RAM it is allocated. As a result, customers may be paying more on a per EC2-Instance basis. Customers who are able to identify opportunitites for rightsizing EC2 Instances can typically save significantly, especially if the EC2 Instance type chosen represents a large pool of instances. 
* **EBS Volumes**: EBS Volumes are typically a large cost driver for many organizations and are often heavily under-utilized. EBS charges you for the amount of storage you have allocated versus utilize so its important to keep an eye on Volume utilization to rightsize and save accordinly. 
* **RDS Instances**: RDS Instances are similar to EC2 Instances in that they're typically overprovisioned but rarely utilized appropriately. While RDS rightsizing can result in significant cost savings, databases tend to be one of the services that makes sense to leave overprovisioned that you can grow into as downtime for a database during a rightsizing process may not ultimatately be worth the organization cost. 
* **Container Services**: ECS, Fargate and EKS allow you to run services of containers on a pool of underlying EC2 instances either managed by you or managed by AWS if you're using Fargate. Container Services are some of the hardest services to appropriately rightsize but can represent significant saving opportunities, especially for AWS Fargate. 


The first step in rightsizing is to have monitoring and observability in place to even know what your utilization is for these various services. Assuming you feel confident in your usage patterns and how they relate to utilization, your organization can begin to make some decision for potential area to rightsize. 

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-1szz6puz7-zRuJ8J4OJIiBFlcTobYZXA).