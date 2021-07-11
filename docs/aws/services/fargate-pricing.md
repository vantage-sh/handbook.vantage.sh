title: Fargate Pricing | Vantage Cloud Cost Handbook

[Fargate Pricing Page](https://aws.amazon.com/fargate/pricing/)

## Summary

Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). Fargate charges you for the vCPU and Memory for a ECS Task or EKS Pod. Alternatively you can run your own EC2 instances for either EKS or ECS on EC2 which can be significantly cheaper. 

## Pricing Dimensions

* **vCPU Hours**: When configuring a Fargate Task or EKS Pod you assign a certain amount vCPU and are charge a corresponding per-hour VCPU rate. 
* **GB Memory Hours**: When configuring a Fargate Task or EKS Pod you assign a certain amount GB of Memory and are charge a corresponding per-hour GB of Memory rate. 

### Fargate vs self-managed EC2 on ECS or EKS

Fargate charges a significant premium for managing the underlying nodes. Additionally, Fargate has varying degress of vCPU performance that different depending on the Task. As a result, Fargate can have pitfalls relative to self-managed ECS or EKS on EC2 beyond just the additional costs. 

For a more in-depth article for seeing how Fargate is priced relative to self-managed EC2, please read the following blog post for [understanding Fargate pricing](https://www.vantage.sh/blog/fargate-pricing).