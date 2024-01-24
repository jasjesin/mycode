module "vpc" {
  source = "./modules/vpc"

  # mandatory inputs
  name = var.name
  cidr_block = var.cidr_block

  # optional inputs
  instance_tenancy = var.instance_tenancy
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support = var.enable_dns_support
}