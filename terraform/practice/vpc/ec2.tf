
resource "aws_instance" "jas" {
  count     = length(data.aws_subnets.public_jas.ids)
  subnet_id = data.aws_subnets.public_jas.ids[count.index]
  ami       = data.aws_ami.app_ami.id
  #ami                    = var.ami
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.jas_ec2.id]
  user_data              = file("apache_setup.sh")

  lifecycle {
    create_before_destroy = true
  }

  tags = {
    Name = var.name
  }
}
