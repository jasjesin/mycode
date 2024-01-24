resource "aws_default_route_table" "default_rt" {
  default_route_table_id = var.default_route_table_id
  route {
    cidr_block = var.cidr_rt
    gateway_id = var.igw_id
  }

  tags = {
    Name = "${var.name}-default-rt"
  }

  depends_on = [ var.default_route_table_id, var.igw_id ]
}