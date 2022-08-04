# iam-bad-policy
A bad IAM policy for testing [IAM Security Incident Pulumi](https://github.com/djsd123/iam-security-incident-pulumi)

[pulumi]: https://www.pulumi.com/docs/get-started/install/
[Python]: https://www.python.org/downloads/

## Requirements

| Name     | Version            |
|----------|--------------------|
| [Pulumi] | > = 3.8.0, < 4.0.0 |
| [Python] | = 3.9.x            |


## Providers

| Name | Version        |
| ---- |----------------|
| aws  | > = 5.0.0, < 6.0.0 |


## Usage

```shell
export AWS_REGION=<AWS_REGION>
export PULUMI_BACKEND_URL=s3://<YOUR-BUCKET>
```

Create Stack

```shell
pulumi stack init
```

Plan/Preview

```shell
pulumi preview
```

Deploy

```shell
pulumi up
```

Cleanup

```shell
pulumi destroy -y
```
