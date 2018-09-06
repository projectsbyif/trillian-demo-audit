# Trillian Demo: Audit

This demo complements the [traffic data publisher example](https://github.com/projectsbyif/trillian-demo-publish) by validating the signed log root published by the log and running a full audit on the contents of a log. This involves rebuilding the log, recalculating the log root, and comparing it against the signed log root.

## Run

Checkout this repo:

```
git clone https://github.com/projectsbyif/trillian-demo-audit
cd trillian-demo-audit
```

### Configure settings.sh

Copy the `settings.sh.example` file to `settings.sh` and edit it to point it at
the Trillian log you want to push data into.

 - `TRILLIAN_LOG_URL` is the URL of the demo log server, in the form `https://<host>:<port>/v1beta1/logs/<log_id>`
 - `TRILLIAN_LOG_PUBLIC_KEY` is the public key of the Trillian log, which you can query from the log server. It takes the form `<public key algo>:<hash algo>:<der encoded key>`

Look at the [log server](https://github.com/projectsbyif/trillian-demo-server) documentation to find these values for your log.

### Type `make run`

This should set up a virtual environment, install dependencies and run the
demo.
