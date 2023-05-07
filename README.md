![Vantage Picture](https://uploads-ssl.webflow.com/5f9ba05ba40d6414f341df34/5f9bb1764b6670c6f7739564_moutain-scene.svg)

# Cloud Cost Handbook

This is the repository backing the site hosted at [handbook.vantage.sh](http://handbook.vantage.sh/).

The Cloud Cost Handbook is a free, open-source, community-supported set of guides meant to help explain often-times complex pricing of public cloud infrastructure and service providers in "plain english". This guide is is open for anyone to contribute their knowledge to the community. [Vantage](http://vantage.sh/) employees will maintain hosting the guide for everyone and ensure that content is relevant and adheres to styleguides.

The Cloud Cost Handbook is organized into two sections: general concepts and per-service pages.

- **General concepts** are meant to cover topics which apply across multiple different infrastructure service.
- **Per-service pages** are meant to give a brief summary of the service, the pricing dimensions of the service and optionally a list of cost concepts as it relates to that service.

## Contributing Guidelines

Issues and pull requests are welcome for requesting or contributing content. Vantage employees will review all issues and PRs to ensure we're keeping content relevant and up to standard. You're welcome to get in contact with us on our [Slack Community](https://join.slack.com/t/vantagecommunity/shared_invite/zt-1szz6puz7-zRuJ8J4OJIiBFlcTobYZXA) as well where we have a devoted #cloud-cost-handbook channel for discussion as it relates to the handbook.

### Installation

```bash
pip install --user mkdocs
pip install --user mkdocs-material
```

### Deploying

```bash
mkdocs gh-deploy --ignore-version
```

This site leverages [mkdocs](https://www.mkdocs.org/). Prior to opening a pull request, please review your changes locally by running `mkdocs serve` which will allow you to access and review your changes locally at `http://localhost:8000/`.

## Keep Up To Date

Feel free to watch/star this repo as we're looking to update the site regularly with additional services and concepts. Vantage also works on the following relevant projects:

- [EC2Instances.info](https://github.com/vantage-sh/ec2instances.info) - An open-source tool for comparing EC2 instance prices and configurations.
- [The AWS Cost Leaderboard](https://leaderboard.vantage.sh/) - A hosted site of the top AWS cost centers.
- [Vantage](https://vantage.sh/) - A cloud cost transparency platform.
