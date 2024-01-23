resource "aws_launch_configuration" "jas" {
  name_prefix                 = var.name
  image_id                    = data.aws_ami.app_ami.id
  instance_type               = var.instance_type
  security_groups             = ["${aws_security_group.jas_asg.id}"]
  associate_public_ip_address = var.associate_public_ip_address
  user_data                   = file("apache_setup.sh")

  lifecycle {
    create_before_destroy = true
  }

}