resource "aws_vpc" "jas_vpc1" {
  cidr_block = var.cidr_block.vpc
  tags = {
    "Name" = var.team
  }
}
resource "aws_subnet" "jas_public_subnet1" {
  vpc_id = aws_vpc.jas_vpc1.id
  cidr_block = var.cidr_block.subnet1
  availability_zone = var.location.az1
  map_public_ip_on_launch = true
  tags = {
    "Name" = var.team
  }
}
resource "aws_subnet" "jas_public_subnet2" {
  vpc_id = aws_vpc.jas_vpc1.id
  cidr_block = var.cidr_block.subnet2
  availability_zone = var.location.az2
  map_public_ip_on_launch = true
  tags = {
    "Name" = var.team
  }
}
