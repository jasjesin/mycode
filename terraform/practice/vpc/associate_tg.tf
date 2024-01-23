
resource "aws_lb_target_group_attachment" "jas" {
  count            = length(data.aws_instances.jas.ids)
  target_group_arn = aws_lb_target_group.jas.arn
  target_id        = data.aws_instances.jas.ids[count.index]
  port             = var.website
}
