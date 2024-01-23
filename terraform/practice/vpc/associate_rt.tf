
resource "aws_route_table_association" "jas_public_blue" {
  subnet_id      = aws_subnet.jas_public_blue.id
  route_table_id = aws_route_table.jas_public_blue.id
}

resource "aws_route_table_association" "jas_public_green" {
  subnet_id      = aws_subnet.jas_public_green.id
  route_table_id = aws_route_table.jas_public_green.id
}

resource "aws_route_table_association" "jas_pvt_blue_nat_gw" {
  subnet_id      = aws_subnet.jas_pvt_blue.id
  route_table_id = aws_route_table.jas_pvt_blue_subnet.id
}

resource "aws_route_table_association" "jas_pvt_green_nat_gw" {
  subnet_id      = aws_subnet.jas_pvt_green.id
  route_table_id = aws_route_table.jas_pvt_green_subnet.id
}
