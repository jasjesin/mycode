resource "aws_default_route_table" "jas_igw" {
  default_route_table_id = aws_vpc.jas.default_route_table_id
  route {
    cidr_block = var.cidr_rt
    gateway_id = aws_internet_gateway.jas.id
  }

  tags = {
    Name = var.name
  }
}