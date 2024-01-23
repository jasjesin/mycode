
resource "aws_lb" "jas" {
  subnets         = data.aws_subnets.public_jas.ids
  security_groups = [aws_security_group.jas_elb.id]

  tags = {
    Name = var.name
  }
}
