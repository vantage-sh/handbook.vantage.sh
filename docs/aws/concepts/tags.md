title: Tagging Resources

Tags are one of the most powerful (though often overlooked) tools that can assist with your ability to observe and allocate cloud costs related to public cloud infrastructure providers like AWS, Azure, and GCP. While different accounts can be useful for separating resources and costs across different environments (production, staging, QA, test, etc.) or teams/business units, tags are helpful for segmenting costs related to your application. We encourage customers to adopt tagging strategies as early on as possible in their organizations. Similar to an effective unit testing suite, over time tags can give you confidence in understanding where your costs are coming from.

Tags in AWS consist of two different parts: a `key` and a `value`. As a basic example, you can imagine an example `key` with the value of "service" and a `value` that could be "front-end", "back-end", "search" or "cache". Upon assigning tags to resources, you can get greater visibility into where your costs are coming from. Instead of seeing how your costs are trending in aggregate, you can see how each part of your application is growing, assuming you've leveraged tags correctly. Additionally, tags can be part of your existing workflows and are typically very easy to accommodate in infrastructure-as-code configuration files such as CloudFormation or Terraform.

Tags, at their core, are metadata attached to cloud resources. They serve as markers, providing context and categorization. Beyond just identification, tags play a pivotal role in:

**Cost Allocation:** Understand which department, project, or application consumes resources and incurs costs.

**Cost Optimization:** Identify underutilized resources and make informed decisions about scaling or termination.

**Forecasting:** Predict future expenses by analyzing tagged resource consumption.

**Resource Management:** Efficiently manage, search, and filter resources based on specific criteria.

**Security and Compliance:** Ensure resources meet specific security standards or compliance requirements.

**Operational Clarity:** Quickly identify resources during troubleshooting or operational tasks.

**Alerting:** Set event-based notifications for specific resources.

**Automation:** Automate lifecycle management or schedule shutdowns.

## Activating Cost Allocation Tags

One of the more generally confusing experiences that customers experience with AWS is that tags are not incorporated into billing reports by default and need to be activated. After you have assigned tags to resources, here are the steps to activate the tags for them to be incorporated into billing data:

To activate your tags:

- Sign in to the AWS Management Console and open the [Billing and Cost Management Console](https://console.aws.amazon.com/billing/home?#/tags).
- In the navigation pane, choose `Cost Allocation Tags`.
- Select the tags that you want to activate.
- Choose `Activate`.

After you create and apply tags to your resources, it can take up to 24 hours for the tags to appear in your reports. Then, after you select your tags for activation, it can take up to 24 hours for the tags to activate.

## Types of Tags

Distinguishing between tag types can help in understanding their origin and purpose. AWS-generated tags are system-defined, providing metadata like creation time or AWS service specifics. User-generated tags are defined by users, tailored to organizational needs, and can be as diverse as the business demands.

While customization is key, starting with commonly used tags can provide a foundational framework:

- **Environment:** Differentiate between Development, Testing, and Production.
- **Owner:** Pinpoint responsibility, aiding in accountability and management.
- **Project:** Allocate resources to specific initiatives or campaigns.
- **Cost Center / Business Unit:** Facilitate financial reporting and budget allocation.
- **Service:** Categorize resources based on the service they support or belong to.
- **Customer:** Especially for SaaS providers, understand resource consumption per client.
- **Function:** Understand the role or purpose of a resource in the ecosystem.

## Tagging Strategy

A tagging strategy is not a one-size-fits-all solution. It requires careful consideration of stakeholder needs, cloud complexity, and automation capabilities. We recommend engaging with finance, operations, and development departments to understand their reporting and management needs.

A multi-cloud or hybrid cloud environment might require a more nuanced approach for tagging. For example, you may want to align tag values across Datadog and AWS so that you can group costs across providers for a single service together.

Utilize tools and scripts to automate tagging for consistency and efficiency. Several types of reports can be built with cloud cost management tools to show you which resources are not tagged so you can make progress.

To harness the full potential of tags, maintain consistency with a clear naming convention and stick to it. Tools like AWS Tag Editor or infrastructure-as-code solutions like Terraform, Pulumi, or CloudFormation can help enforce tagging. After the initial setup, make sure to review regularly. As the organization evolves, so will its tagging needs. Periodic reviews ensure relevance. To ensure the stickiness of the strategy, educate and train team members so they understand the importance of tagging and how to do it correctly.

## Implementing Tagging

It’s rare to plan and launch a tagging strategy from scratch. More likely than not, a company already has some infrastructure tagging, and a need to improve this visibility for deeper cost visibility. When implementing a new tagging program that adds or replaces existing tags, we recommend a few collaborative approaches.

Firstly, there should be an audit of existing tags. Decide what tags to keep and which to ignore, and measure the accuracy of what tags exist. Then, identify untagged resources. Measure how much of your infrastructure is untagged, and use that to track progress as the program progresses. In the process, you will want to partner with engineering. Clearly communicate new tagging guidelines, and support engineers owning the work to tag infrastructure. Finally, gamify the process. Find ways to recognize or reward teams as tagging work is completed.

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).
