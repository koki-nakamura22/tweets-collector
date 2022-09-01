terraform {
  required_version = "1.2.8"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>4.0"
    }
  }
}

provider "aws" {
  profile = "terraform"
  region  = "ap-northeast-1"
}

# --------------------------
# SSM Parameter Store
# --------------------------
variable "twitter_api_key" {
  type = string
}

variable "twitter_api_secret_key" {
  type = string
}

variable "twitter_bearer_token" {
  type = string
}

variable "twitter_access_token" {
  type = string
}

variable "twitter_access_token_secret" {
  type = string
}

resource "aws_ssm_parameter" "twitter_api_key" {
  name = "twitter_api_key"
  type = "String"
  value = var.twitter_api_key
}

resource "aws_ssm_parameter" "twitter_api_secret_key" {
  name = "twitter_api_secret_key"
  type = "String"
  value = var.twitter_api_secret_key
}

resource "aws_ssm_parameter" "twitter_bearer_token" {
  name = "twitter_bearer_token"
  type = "String"
  value = var.twitter_bearer_token
}

resource "aws_ssm_parameter" "twitter_access_token" {
  name = "twitter_access_token"
  type = "String"
  value = var.twitter_access_token
}

resource "aws_ssm_parameter" "twitter_access_token_secret" {
  name = "twitter_access_token_secret"
  type = "String"
  value = var.twitter_access_token_secret
}

# --------------------------
# S3 bucket
# --------------------------
variable "lambda_role_arn" {
  type = string
}

resource "aws_s3_bucket" "s3_deploy_bucket" {
  bucket = "tweets-collector"

  versioning {
    enabled = false
  }
}

resource "aws_s3_bucket_public_access_block" "s3_deploy_bucket" {
  bucket                  = aws_s3_bucket.s3_deploy_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
  depends_on = [
    aws_s3_bucket_policy.s3_deploy_bucket
  ]
}

resource "aws_s3_bucket_policy" "s3_deploy_bucket" {
  bucket = aws_s3_bucket.s3_deploy_bucket.id
  policy = data.aws_iam_policy_document.s3_deploy_bucket.json
}

data "aws_iam_policy_document" "s3_deploy_bucket" {
  statement {
    effect    = "Allow"
    actions   = ["s3:GetObject", "s3:PutObject"]
    resources = ["${aws_s3_bucket.s3_deploy_bucket.arn}/*"]
    principals {
      type        = "AWS"
      identifiers = [var.lambda_role_arn]
    }
  }
}
