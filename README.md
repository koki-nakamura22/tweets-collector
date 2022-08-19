# tweets-collector

## Set up

### Set up AWS credentials

```sh
serverless config credentials --provider aws --key [Access key] --secret [Secret access key]
```

### Install plugins

```sh
sls plugin install -n serverless-prune-plugin
sls plugin install -n serverless-s3-local
sls plugin install -n serverless-local-schedule
```
