
data "aws_vpc" "jas" {
  filter {
    name   = "tag:Name"
    values = ["jas"]
  }
}

data "aws_internet_gateway" "jas" {
  filter {
    name   = "tag:Name"
    values = ["jas"]
  }
}


data "aws_subnet" "jas_public_blue" {
  filter {
    name   = "tag:Name"
    values = ["jas_public_blue"]
  }
}


data "aws_subnet" "jas_public_green" {
  filter {
    name   = "tag:Name"
    values = ["jas_public_green"]
  }
}

data "aws_subnets" "public_jas" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.jas.id]
  }

  filter {
    name   = "tag:Name"
    values = ["jas_public_blue", "jas_public_green"]
  }
}

data "aws_subnets" "pvt_jas" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.jas.id]
  }

  filter {
    name   = "tag:Name"
    values = ["jas_pvt_blue", "jas_pvt_green"]
  }
}

data "aws_ami" "app_ami" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*"]
  }
}

data "aws_region" "current_region" {
}

data "aws_instances" "jas" {
  instance_state_names = ["running"]
}