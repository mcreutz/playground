terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-central-1"
}

# create a cloudwatch dashboard
resource "aws_cloudwatch_dashboard" "example" {
  dashboard_name = "example-dashboard"
  dashboard_body = file("${path.module}/example_dashboard.json")
}
