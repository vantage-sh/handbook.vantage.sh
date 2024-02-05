title: Snowflake Cloud Services and Adjustments | Cloud Costs Handbook

[Snowflake Cloud Services Costs Documentation](https://docs.snowflake.com/en/user-guide/cost-understanding-compute#cloud-service-credit-usage){ .md-button }

You may have seen an "Adjustment for Cloud Services" on a Snowflake bill and wondered why it was negative—or you may be seeing unexpected charges in the "Cloud Services" category. Cloud services are a separate pricing dimension for Snowflake that are reported on but not included in your bill, except in certain cases.

![Snowflake adjustments for cloud services](/img/snowflake/snowflake-cloud-services.png)

## Cloud Services Adjustment: The 10% Threshold

Cloud services are services that coordinate various activities across Snowflake. Basically, they're everything that is not involved in running queries or storing data. Most likely, the heaviest cloud service usage will come from:

* Metadata management
* Query parsing and optimization
* SQL API

Snowflake starts billing for cloud services only after they exceed 10% of your warehouse compute credit cost. Let's say you spend $100 on Snowflake queries and $9 on cloud services. Your total bill will be $100. But if you spent $19 on cloud services, your bill would be $109. This threshold is recalculated every day for the current day's warehouse compute credit usage.

## Tips for Reducing Cloud Services Costs

The following common data operations consume cloud services on Snowflake. You can follow recommended patterns to avoid them.

* **Full clones:** Consider selectively cloning your databases for development, ETL, or backup purposes. Cloning consumes only cloud services credits, so if you run a large clone operation on the same day when fewer queries are run, you will pay. Instead, you can clone only the tables you need to stay under the 10% threshold.
* **Fragmented schemas:** Snowflake does not recommend using schema design techniques from Hadoop, OLTP, or NoSQL databases where you may have denormalized data spread out across multiple schemas. Instead, use one schema to minimize metadata lookups.
* **Very complex queries:** The query optimization software Snowflake runs is broken out into cloud services. So if you write SQL queries that are thousands of lines long, or contain many joins or excessive recursion, you may find yourself with higher cloud services costs.
* **Excessively frequent queries:** Lastly, the SQL API handles the ingestion of each SQL query internally. Requesting this API (running queries) tens of thousands of times per day will start to result in charges.

It's possible that these issues may be caused by third-party services running on Snowflake and not your team itself. You can explicitly monitor the queries your company is running by adding [query tagging](https://www.vantage.sh/blog/snowflake-costs-per-query-using-query-tags). You can also [review additional tips](https://www.vantage.sh/blog/snowflake-compute-costs) for saving on your Snowflake compute bills.

</br>

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).