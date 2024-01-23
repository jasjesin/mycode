resource "aws_autoscaling_group" "jas" {
  launch_configuration = aws_launch_configuration.jas.id
  min_size             = var.min
  max_size             = var.max
  target_group_arns    = ["${aws_lb_target_group.jas_asg.arn}"]
  vpc_zone_identifier  = data.aws_subnets.public_jas.ids

  tag {
    key                 = var.key
    value               = var.name
    propagate_at_launch = true
  }
}