
resource "aws_route_table" "jas_pvt_blue_subnet" {
  vpc_id = data.aws_vpc.jas.id
  route {
    cidr_block     = var.cidr_rt
    nat_gateway_id = aws_nat_gateway.jas_blue.id
  }

  tags = {
    Name = var.name_pvt_blue
  }
}

resource "aws_route_table" "jas_pvt_green_subnet" {
  vpc_id = data.aws_vpc.jas.id
  route {
    cidr_block     = var.cidr_rt
    nat_gateway_id = aws_nat_gateway.jas_green.id
  }

  tags = {
    Name = var.name_pvt_green
  }
}