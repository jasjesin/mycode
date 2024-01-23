
resource "aws_lb_listener" "jas" {
  load_balancer_arn = aws_lb.jas.arn
  port              = var.website
  protocol          = var.http_protocol
  default_action {
    type = var.listener_type
    forward {
      target_group {
        arn = aws_lb_target_group.jas.arn
      }
      stickiness {
        enabled  = var.stickiness
        duration = var.stickiness_duration
      }
    }
  }
}
