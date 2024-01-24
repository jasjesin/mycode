resource "aws_vpc" "vpc" {
  cidr_block           = var.cidr_block
  instance_tenancy     = var.instance_tenancy
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support   = var.enable_dns_support

  tags = {
    Name = "${var.name}-vpc"
  }
}

module "igw" {
  source = "./igw"
  vpc_id = aws_vpc.vpc.id
  name = var.name
}

module "default_rt" {
  source = "./default_rt"
  default_route_table_id = aws_vpc.vpc.default_route_table_id
  igw_id = module.igw.igw_id
  name = var.name
}
