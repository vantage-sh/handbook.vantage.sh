Tags are one of the most powerful (though often overlooked) tools that can assist with your ability to observe and allocate cloud costs as it relates to public cloud infrastructure providers like AWS, Azure and GCP. While different AWS accounts can be useful for separating resources and costs across different environments (production, staging, qa, test, etc) or teams/business-units, tags are helpful for segmenting costs as it relates to your application. We encourage customers to adopt tagging strategies as early on at their organizations as possible. Similar to an effective unit testing suite, over time tags can give you confidence in understanding where your costs are coming from. 

Tags on AWS consist of two different parts: a `key` and a `value`. As a basic example you can imagine an example `key` with the value of "service" and potential `value`s of "front-end", "back-end", "search" or "cache". Upon assigning tags to resources, you can get greater visibility into where your costs are coming from. Instead of seeing how your costs are trending in aggregate, you can see how each part of your application is growing assuming you've leveraged tags correctly. Additionally, tags can be part of your existing workflows and are typically very easy to accomodate in infrastructure-as-code configuration files such as CloudFormation or Terraform. 

## Activating Cost Allocation Tags

One of the more generally confusing experiences that customers experience on AWS is that tags are not incorporated into billing reports by default and need to be "activated". After you have assigned resources tags, here are the steps to "activate" the tags for them to be incorporated into billing data:

To activate your tags

* Sign in to the AWS Management Console and open the Billing and Cost Management console at [https://console.aws.amazon.com/billing/home?#/tags](https://console.aws.amazon.com/billing/home?#/tags).
* In the navigation pane, choose Cost Allocation Tags.
* Select the tags that you want to activate.
* Choose Activate.

After you create and apply tags to your resources, it can take up to 24 hours for the tags to appear in your reports. After you select your tags for activation, it can take up to 24 hours for tags to activate as well.

!!! Contribute
    Help us improve this page by contributing on [GitHub](https://github.com/vantage-sh/handbook) or discuss the handbook in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-oey52myv-gq4AWRKkX25kjp1UGziPTw).