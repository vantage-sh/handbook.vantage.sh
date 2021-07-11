title: ECR Pricing | Vantage Cloud Cost Handbook

[Amazon ECR Pricing Page](https://aws.amazon.com/ecr/pricing/)

## Summary

Amazon Elastic Container Registry (ECR) is a fully managed container registry that allows you to store container images. You can create as many "Repositories" as you'd like that are free. As you push container "Images" to your repository, you're charged for the storage of these images which can acrue over time. Additionally, ECR charges different data transfer rates for private versus public repositories. 

## Pricing Dimensions

* **Container Image Storage**: Amazon ECR charges a rate per month for the amount of storage per GB you store for container images. 
* **Data Transfer**: Amazon ECR charges different rates for data transfer from public and private repositories. 

## Storage Costs per ECR Repository
Determining the cost per Container Repository can be a lot of effort, especially if you have a large quantity of images. To calculate the storage cost per container repository:

* List all of your container images
* Collect the image digest from each
* Determine just the unique digests of the layers in your container repository
* Get the size of each unique digest.

If you prefer not to do this manually yourself, [Vantage](https://www.vantage.sh/) will compute the size and corresponding cost of all repositories automatically when you connect an AWS account.

## Lifecycle Policies

ECR stores every container image you push to a registry by default. Over time, the storage of all of these images can add up. Amazon offers a primitive called a "Lifecycle Policy" that allows you to set conditions for having Amazon clean up images on your behalf. There are two types of lifeycle policies:

* **imageCountMoreThan**: ECR allows you to define a certain number of images to retain and anything over that count will be cleaned up. For example if you set a Lifecycle Policy with a imageCountMoreThan value of 10, your most recent 10 images will always be kept.
* **sinceImagePushed**: ECR allows you to set lifecycle policies with a value of sinceImagePushed which has a value of a certain number of days. So for example if you have a Lifecycle Policy applied with a sinceImagePushed value of 7, ECR will delete images as often as they are older than 7 days. 

__Note__: that when you apply a Lifecycle Policy, it is evaluated immediately. So if you have 500 images in a repositority and impose a lifeycle policy of 10 as soon as that policy is applied ECR will delete the 490 oldest images. 

### Example `imageCountMoreThan` Lifeycle Policy

Here's an example of how to impose a Lifeycle Policy via the AWS CLI using the value of imageCountMoreThan: 

```
aws ecr put-lifecycle-policy \
    --repository-name "vantage/mcyolo" \
    --lifecycle-policy-text "file://policy.json"

```

Where the content of the file for policy.json is the following:

```
{
  "rules": [
     {
       "rulePriority": 1,
       "description": "Expire images over a count of 10",
       "selection": {
         "tagStatus": "untagged",
         "countType": "imageCountMoreThan",
         "countNumber": 10
       },
       "action": {
         "type": "expire"
       }
     }
  ]
}

```


### Example `sinceImagePushed` Lifeycle Policy


Here's an example of how to impose a Lifeycle Policy via the AWS CLI using the value of sinceImagePushed: 

```
aws ecr put-lifecycle-policy \
    --repository-name "vantage/mcyolo" \
    --lifecycle-policy-text "file://policy.json"

```

Where the content of the file for policy.json is the following:

```
{
  "rules": [
     {
       "rulePriority": 1,
       "description": "Expire images older than 14 days",
       "selection": {
         "tagStatus": "untagged",
         "countType": "sinceImagePushed",
         "countUnit": "days",
         "countNumber": 14
       },
       "action": {
         "type": "expire"
       }
     }
  ]
}

```