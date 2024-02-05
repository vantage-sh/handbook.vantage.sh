title: Cost Reports | Cloud Costs Handbook

[Cost Reports](https://vantage.sh/features/cost-reports) are multi-dimensional reports for finding and tracking costs. How to use Cost Reports is covered in the [Vantage documentation](https://docs.vantage.sh/cost_reports/). This page will focus on a compendium of specific types of reports that are helpful for controlling cloud costs.

## Report Examples

These use cases have come up repeatedly in the cloud costs community. Contributors are encouraged to add more as they see fit.

### Untagged Resources

![Untagged](https://assets.vantage.sh/blog/governance/untagged-resources.png)

Many organizations use [tags](/aws/concepts/tags) to keep track of all their cloud resources. For practitioners, keeping the percentage of untagged resources low means greater visibility inside cost tools. [Tags must be enabled](https://www.vantage.sh/blog/aws-cost-explorer#cost-by-tagged-resources) to be used in Cost Reports.

### Showback Report

![Showback](https://assets.vantage.sh/blog/showback-cost-allocation/showback-cost-allocation-2.png)

Shared resources like support or a database cluster make divvying up costs among teams difficult. Use the Cost Allocation tool to create a Showback or Chargeback report for transparent reporting.

### Compute Costs without Data

![No data](https://pbs.twimg.com/media/FVK0WgJXoAEVqCS?format=png&name=small)

Very active data teams generate costs as well as insights. For measuring just the cost to deliver software, exclude these costs from a report.

### Just Data Egress

![Data egress](/img/tools/cost-reports/data-egress.gif)

Data egress is famously the third cost category of AWS that is very significant for teams, alongside compute and storage. Using subcategories, it is possible to see data egress costs per service.

### Redshift Instance Costs

![Redshift instances](/img/tools/cost-reports/redshift.png)

EC2 instances power multiple managed services inside AWS. To reveal these, save the Report first then click on the drill-down button on any row. In this example, we are inspecting Redshift instance costs.

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).
