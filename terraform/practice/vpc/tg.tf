
resource "aws_lb_target_group" "jas" {
  name        = var.name
  port        = var.website
  protocol    = var.http_protocol
  vpc_id      = data.aws_vpc.jas.id
  target_type = var.tg_type
}

resource "aws_lb_target_group" "jas_asg" {
  name        = var.name_asg
  port        = var.website
  protocol    = var.http_protocol
  vpc_id      = data.aws_vpc.jas.id
  target_type = var.tg_type
}
