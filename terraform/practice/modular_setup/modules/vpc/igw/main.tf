resource "aws_internet_gateway" "igw" {
  vpc_id = var.vpc_id

  tags = {
    Name = "${var.name}-igw"
  }

  depends_on = [ var.vpc_id ]
}
