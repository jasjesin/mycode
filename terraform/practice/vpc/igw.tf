resource "aws_internet_gateway" "jas" {
  vpc_id = aws_vpc.jas.id

  tags = {
    Name = var.name
  }
}