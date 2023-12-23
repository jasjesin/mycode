resource "aws_route_table" "jas_rt1" {
  vpc_id = aws_vpc.jas_vpc1.id
  route  {
    cidr_block = var.cidr_block.outside
    gateway_id = aws_internet_gateway.jas_igw1.id
  }
  tags = {
    "Name" = var.team
  }
}

resource "aws_route_table_association" "jas_rt_public_subnet1" {
  subnet_id = aws_subnet.jas_public_subnet1.id
  route_table_id = aws_route_table.jas_rt1.id
}
