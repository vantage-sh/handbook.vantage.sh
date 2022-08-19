title: Snowflake Cloud Services and Adjustments | Cloud Costs Handbook

[Snowflake Cloud Services Costs Documentation](https://docs.snowflake.com/en/user-guide/credits.html#cloud-services-credit-usage){ .md-button }

You may have seen an 'Adjustment for Cloud Services' on a Snowflake bill and wondered why it was negative. Or you may be seeing unexpected charges in the Cloud Services category. Cloud Services are a separate pricing dimension for Snowflake that are reported on but not included in your bill, except in certain cases.

![Snowflake adjustments for cloud services](/img/snowflake/snowflake-cloud-services.png)

## Cloud Services Adjustment: The 10% Threshold

Cloud services are a "collection of services that coordinate activities across snowflake". Basically, it's everything that is not involved in running queries or storing data. Most likely, the heaviest cloud service usage will come from:

* Metadata management
* Query parsing and optimization
* SQL API

Snowflake only starts billing for Cloud Services after they exceed 10% of your compute credits cost. Let's say you spend $100 on Snowflake queries and $9 on cloud services. Your total bill will be $100. But if you spent $19 on cloud services, your bill would be $109. This threshold is recalculated every day for the current day's compute credit usage.

## Tips for Reducing Cloud Services Costs

The following common data operations consume cloud services on Snowflake and there are recommended patterns to avoid them.

* **Full clones.** Consider selectively cloning your databases for development, ETL, or backup purposes. Cloning only consumes cloud credits, so if you run a large clone operation on the same day when fewer queries are run, you will pay. Instead, you can clone only the tables you need to stay under the 10% threshold.
* **Fragmented schemas.** Snowflake does not recommend using schema design techniques from Hadoop, OLTP, or NoSQL databases where you may have denormalized data spread out amongst multiple schemas. Instead use one schema to minimize metadata lookups.
* **Very complex queries.** The query optimization software snowflake runs is broken out into cloud services. So if you write SQL queries that are thousands of lines long, or contain many JOINs or excessive recursion you may find yourself with higher cloud services costs.
* **Excessively frequent queries.** Lastly, the SQL API handles the ingestion of each SQL query internally. Requesting this API (running queries) tens of thousands of times per day would start to result in charges.

It's possible that these issues may be caused by third party services running on Snowflake and not your team itself. You can monitor explictly the queries that your company is running by adding [query tagging](https://www.vantage.sh/blog/snowflake-costs-per-query-using-query-tags). For more scenarios like the ones above, please contribute to this page or review more [Snowflake resources](https://community.snowflake.com/s/article/Cloud-Services-Billing-Update-Understanding-and-Adjusting-Usage) on optimizing Cloud Services costs.

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://join.slack.com/t/vantagecommunity/shared_invite/zt-oey52myv-gq4AWRKkX25kjp1UGziPTw).