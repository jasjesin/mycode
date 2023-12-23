resource "aws_internet_gateway" "jas_igw1" {
  vpc_id = aws_vpc.jas_vpc1.id
  tags = {
    "Name" = var.team
  }
}