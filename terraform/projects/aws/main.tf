provider "aws" {
  region     = var.region
#  access_key = data.local_file.access_key.content
#  secret_key = data.local_file.secret_key.content
}

# Create following resources
# 1. VPC
# 2. IG
# 3. Route Table (Associate Subnet to Route Table)
# 4. Subnet
# 5. Associate Subnet with Route Table
# 6. SG to allow ports 22, 80, 443
# 7. Network Interface wid IP in subnet, that is created in Step 4
# 8. Assign elastic IP to network interface, created in Step 7
# 9. Create Linux server and install/enable Apache2

# 1. VPC
resource "aws_vpc" "vpc" {
  cidr_block = var.cidr_blocks[0]
  tags = {
    "Name" = var.environment
  }
}

# 2. IG
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.vpc.id 

  tags = {
    Name = var.environment
  }
}

# 3. Route Table (Associate Subnet to Route Table)
resource "aws_route_table" "route_table" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = var.cidr_blocks[2]
    gateway_id = aws_internet_gateway.gw.id
  }

  route {
    ipv6_cidr_block        = var.cidr_blocks[3]
    egress_only_gateway_id = aws_internet_gateway.gw.id
  }

  tags = {
    Name = var.environment
  }
}

# 4. Subnet
resource "aws_subnet" "subnet-1" {
  vpc_id = aws_vpc.vpc.id
  cidr_block = var.cidr_blocks[0]
  tags = {
    "Name" = var.environment
  }
}

# 5. Associate Subnet with Route Table

# 6. SG to allow ports 22, 80, 443
# 7. Network Interface wid IP in subnet, that is created in Step 4
# 8. Assign elastic IP to network interface, created in Step 7

# 9. Create Linux server and install/enable Apache2
resource "aws_instance" "webserver" {
  ami = "${data.aws_ami.amazon-linux-2.id}"
  instance_type = var.instance_type
  lifecycle {
    create_before_destroy = true
  }
  tags = {
    "Name" = var.webserver
  }
}

# 10. ALB
# 11. ASG




data "local_file" "access_key" {
  filename = "/Users/jasdil/Documents/Learnings/terraform/creds/aws/access_key"
}

data "local_file" "secret_key" {
  filename = "/Users/jasdil/Documents/Learnings/terraform/creds/aws/secret_key"
}

data "aws_ami" "amazon-linux-2" {
  most_recent = true

  filter {
    name   = "owner-alias"
    values = ["amazon"]
  }

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-ebs"]
  }
}