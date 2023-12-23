terraform {
  required_version = ">=1.3.6"
}

provider "aws" {
  region = "us-west-1"
}

resource "aws_vpc" "vpc1" {
  cidr_block = "10.1.0.0/16"
  tags = {
      Name = "jas_vpc1"
  }
}

resource "aws_subnet" "public_subnet1" {
    vpc_id = aws_vpc.vpc1.id
    cidr_block = "10.1.1.0/24"
    availability_zone = "us-west-1b"
    tags = {
        Name = "jas_public_subnet1"
  }  
}

resource "aws_internet_gateway" "igw1" {
      vpc_id = aws_vpc.vpc1.id

      tags = {
        "Name" = "jas_igw1"
      }
}

resource "aws_route_table" "gtwy_rt" {
    vpc_id = aws_vpc.vpc1.id
    route {
      cidr_block = "0.0.0.0/0"
      gateway_id = aws_internet_gateway.igw1.id
    }

    tags = {
      "Name" = "jas_gtwy_rt1"
    }
  
}

resource "aws_route_table_association" "gtwy_rt_association" {
  subnet_id = aws_subnet.public_subnet1.id
  route_table_id = aws_route_table.gtwy_rt.id
}

resource "aws_instance" "ec2_ins1" {
  ami = "ami-00d8a762cb0c50254"
  instance_type = "t2.micro"
  tags = {
    "Name" = "jas_ec2_ins1"
  }
}

resource "aws_eip" "eip1" {
  tags = {
    "Name" = "jas_eip1"
  }
}