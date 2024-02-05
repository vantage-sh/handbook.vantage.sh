title: Instances Pricing Documentation | Cloud Cost Handbook

[AWS Instance Types Comparison](https:/instances.vantage.sh/){ .md-button }

[EC2Instances.info](https://instances.vantage.sh) shows current pricing for AWS EC2, RDS, and ElastiCache instances. The tool is completely [open source](https://github.com/vantage-sh/ec2instances.info) and uses the same Amazon APIs available to everyone. Development for Instances is coordinated through the [Vantage Slack](https://vantage.sh/slack/) as well as on [Github](https://github.com/vantage-sh/ec2instances.info).

## Why?

Because it's frustrating to compare instances using Amazon's own [instance type](http://aws.amazon.com/ec2/instance-types/), [pricing](http://aws.amazon.com/ec2/pricing/), and other pages.

## Columns and Filters

![Columns and Filters](/img/tools/instances/column_selector.png)

Nearly every service attribute available for a specific instance is available, although most are hidden by default. You can add more attributes, for example GPUs, in by clicking the `Columns` dropdown. Other dropdowns allow for selecting the `Region`, changing the per-unit basis of calculation (e.g. for vCPUs), and changing the term of the `Reserved` instance purchase.

For each column that is shown, it can be further filtered using simple glob matching, and the entire table can be searched using the top right search box.

### Regex Support

![Filter EC2 instances by Regex](/img/tools/instances/regex-filter.png)

Each column and the top right search bar support regex expressions. So you can enter an expression like this: `[rt][3456].?.larg` and the resulting rows will be a mix of t and r instances as shown above.

## Comparing Instances

![Compare instances](/img/tools/instances/compare_selected.gif)

By clicking on an individual row in the table, you can select it to be compared with other rows. You can do this while filtering as well. Click `Compare Selected` and only the selected rows will be shown. The URL is also changed so this specific comparison can be shared with others.

## Detail Pages

![Detail Pages](/img/tools/instances/detail-pages.png)

For EC2 and RDS, the "API Name" column contains clickable links to each instance type. The Detail Page for the instance is essentially a pivot of the main table, with some additional tools to make the information more digestible.

### Pricing Widget

In the upper left, a pricing widget has selectors for calculating the estimated cost of the instance in different regions, over different amounts of time, or for different software that runs on the instance. When the price is shown as "N/A" that indicates that the instance is not available to purchase with the combination of selectors.

### Instance Attributes

In the middle of each Detail Page are the major categories of attributes and their values. These attributes are all selectable as columns in the main Instances pages. To request more attributes, click "Open a ticket" in the bottom right.

## Saving and Clearing Filters

Instances automatically saves the filters and selections that are applied to local storage. This means that when you open a new session you will be greeted with the most recent set of filters and columns. This can be helpful for working on services which mostly use the same types of instances.

To reset the table, click `Clear Filters`.

## Export Data

The table, with its filters applied, sorted, and with columns shown and hidden, can be exported exactly as a CSV. Data for EC2 is also available for free from the [Vantage API](https://vantage.readme.io/reference/general).

## Azure Support (Beta)

[Azure VM types pricing and comparison](https://instances.vantage.sh/azure) is also available (Beta). Switch to Azure in the bottom left corner of the page.

## Contributors

EC2Instances.info was started by [@powdahound](http://twitter.com/powdahound), contributed to by [many](https://github.com/vantage-sh/ec2instances.info/contributors), is now managed and maintained by [Vantage](https://vantage.sh/) and awaits your improvements on [GitHub](https://github.com/vantage-sh/ec2instances.info). In the development of Detail Pages, we used components of designs from [cloudhw.info](https://cloudhw.info/) with permission from [Joshua Powers](https://powersj.io/).

## Warning

EC2Instances.info is not maintained by or affiliated with Amazon. The data shown is not guaranteed to be accurate or current. Please [report issues](http://github.com/vantage-sh/ec2instances.info/issues) you see.

!!! Contribute
Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).
