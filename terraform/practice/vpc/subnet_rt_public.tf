
resource "aws_route_table" "jas_public_blue" {
  vpc_id = data.aws_vpc.jas.id
  route {
    cidr_block = var.cidr_rt
    gateway_id = data.aws_internet_gateway.jas.id
  }

  tags = {
    Name = var.name_public_blue
  }
}

resource "aws_route_table" "jas_public_green" {
  vpc_id = data.aws_vpc.jas.id
  route {
    cidr_block = var.cidr_rt
    gateway_id = data.aws_internet_gateway.jas.id
  }

  tags = {
    Name = var.name_public_green
  }
}
