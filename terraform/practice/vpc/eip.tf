resource "aws_eip" "jas_blue" {

  tags = {
    Name = var.name_public_blue
  }
}

resource "aws_eip" "jas_green" {

  tags = {
    Name = var.name_public_green
  }
}