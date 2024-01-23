
resource "aws_nat_gateway" "jas_blue" {
  allocation_id = aws_eip.jas_blue.id
  subnet_id     = data.aws_subnet.jas_public_blue.id

  tags = {
    Name = var.name
  }
}


resource "aws_nat_gateway" "jas_green" {
  allocation_id = aws_eip.jas_green.id
  subnet_id     = data.aws_subnet.jas_public_green.id

  tags = {
    Name = var.name
  }
}