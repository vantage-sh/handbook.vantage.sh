title: Elastic Load Balancer Pricing | Vantage Cloud Cost Handbook

[Amazon ELB Pricing Page](https://aws.amazon.com/elasticloadbalancing/pricing/){ .md-button }

## Summary

Amazon Elastic Load Balancer (ELB) is a service which distributes traffic from a single endpoint (public or private) to one or many private resources. Most commonly an Elastic Load Balancer will be exposed to the public internet and will distribute the incoming traffic to several app servers (usually running on EC2 or ECS). Elastic Load Balancers can also be used to distribute private traffic from one service to another. There are different options for the type of ELB and they are priced differently and come with different feature sets.

## Pricing Dimensions

| Dimension | Description |
| -- | -- |
| Load Balancer Hours | Every type of load balancer has a standard per hour rate and is always billed for a full hour. |
| Load Balancer Data Processed | Each type of load balancer has a formula for how the data processed by the load balancer is turned into an additional hourly charged. |

## Application Load Balancer
Application Load Balancers are useful for distributing layer 7 (HTTP, HTTPS, gRPC) traffic to application servers or other backends. ALBs have a standard hourly rate per region and a formula for calculating "LCU"-hours. The dimensions for calculating LCU are:

| Dimension | Description |
| ---------- | -- |
| New Connections | a single LCU is 25 new connections per second |
| Active connections | a single LCU is 3,000 active connections per minute |
| Processed bytes | a single LCU is 1 GB per hour for EC2 instances, containers and IP addresses as targets and 0.4 GB per hour for Lambda functions as targets |
| Rule evaluations | a single LCU is 1,000 rule evaluations per second |

Whichever of these dimensions produces the highest LCU for an hour is what is used to create the charge for LCU-hour.

## Network Load Balancer
Network Load Balacers are used for forwarding layer 4 traffic (TCP, UDP, TLS) to any other resoruce with an ip address. NLBs have a standard hourly rate per region and a formula for calculating "NLCU"-hours depending on the type of network traffic. The dimensions for calculating NCLU are:

| Dimension   | TCP         | UDP | TLS |
| ----------- | ----------- |-----|-----|
| New Connection or Flow | 800 | 400 | 50 |
| Active Connection or Flow | 100,000 | 50,000 | 3,000 |
| Processed bytes | 1GB | 1GB | 1GB |
 

## Gateway Load Balancer
Gateway Load Balancers are used to proxy traffic through third-party virtual appliances which support GENEVE. GLBs have a standard hourly rate per region and a formula for calculating "GLCU"-hours. The dimensions for calculating GLCU are:

| Dimension | Description |
| ---------- | -- |
| New Connections | a single LCU is 600 new connections per second |
| Active connections | a single LCU is 60,000 active connections per minute |
| Processed bytes | a single LCU is 1 GB per hour for EC2 instances, containers and IP addresses as targets and 0.4 GB per hour for Lambda functions as targets |

## Classic Load Balancer
Classic load balancers are the original type of load balancer which has since been superceded by ALB and NLB. CLBs support both layer 7 and layer 4 traffic. CLBs have a standard hourly rate per region and a standard per GB rate per region for traffic processed. 

<br/>

!!! Contribute
	Help us improve this page by making a contribution on our [Github repository](https://github.com/vantage-sh/handbook).