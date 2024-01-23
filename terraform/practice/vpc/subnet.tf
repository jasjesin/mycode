
resource "aws_subnet" "jas_public_blue" {
  vpc_id                  = data.aws_vpc.jas.id
  cidr_block              = var.cidr_public_blue_subnet
  availability_zone       = var.availability_zone_blue
  map_public_ip_on_launch = var.map_public_ip_on_launch

  tags = {
    Name = var.name_public_blue
  }
}

resource "aws_subnet" "jas_public_green" {
  vpc_id                  = data.aws_vpc.jas.id
  cidr_block              = var.cidr_public_green_subnet
  availability_zone       = var.availability_zone_green
  map_public_ip_on_launch = var.map_public_ip_on_launch

  tags = {
    Name = var.name_public_green
  }
}

resource "aws_subnet" "jas_pvt_blue" {
  vpc_id            = data.aws_vpc.jas.id
  cidr_block        = var.cidr_pvt_blue_subnet
  availability_zone = var.availability_zone_blue

  tags = {
    Name = var.name_pvt_blue
  }
}


resource "aws_subnet" "jas_pvt_green" {
  vpc_id            = data.aws_vpc.jas.id
  cidr_block        = var.cidr_pvt_green_subnet
  availability_zone = var.availability_zone_green

  tags = {
    Name = var.name_pvt_green
  }
}
