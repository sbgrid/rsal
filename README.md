# RSAL
## Repository Storage Abstraction Layer

### Overview
This is an abstraction layer for dataset storage, designed to integrate with repository software.
More particularly, for mediating network access to datasets without going through the repository application server, and allowing for access through non-http protocols.

So what does it actually *do*?
RSAL listens for a signal from Dataverse (in the default case, a http request from a pre-publication workflow), takes the necessary steps for users to be able to download the datafiles from that dataset (in Dataverse context, this is currently assumed to be a package file), and tells Dataverse to resume the workflow.


### Installation
See [installation instructions](doc/installation.md) for RSAL installation instructions, and the [Dataverse Guides](http://guides.dataverse.org) for configuring the two systems together.

