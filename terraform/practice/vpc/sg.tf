
resource "aws_security_group" "jas_ec2" {
  name = var.name_ec2
  vpc_id = data.aws_vpc.jas.id

  # allow all external world traffic
  ingress {
    from_port   = var.website
    to_port     = var.website
    protocol    = var.protocol
    cidr_blocks = ["${var.cidr_rt}"]
  }

  # allow traffic from bastion host
  ingress {
    from_port   = var.bastion
    to_port     = var.bastion
    protocol    = var.protocol
    cidr_blocks = ["${var.cidr_rt}"]
  }

  # all traffic allowed for egress
  egress {
    from_port   = var.egress
    to_port     = var.egress
    protocol    = var.protocol_egress
    cidr_blocks = ["${var.cidr_rt}"]
  }

  lifecycle {
    create_before_destroy = true
  }

  tags = {
    Name = var.name
  }
}

resource "aws_security_group" "jas_elb" {
  name = var.name_elb
  vpc_id = data.aws_vpc.jas.id

  ingress {
    protocol    = var.protocol
    from_port   = var.secure
    to_port     = var.secure
    cidr_blocks = ["${var.cidr_rt}"]
  }

  ingress {
    protocol    = var.protocol
    from_port   = var.website
    to_port     = var.website
    cidr_blocks = ["${var.cidr_rt}"]
  }

  # all traffic allowed for egress
  egress {
    from_port   = var.egress
    to_port     = var.egress
    protocol    = var.protocol_egress
    cidr_blocks = ["${var.cidr_rt}"]
  }

  lifecycle {
    create_before_destroy = true
  }
  
  tags = {
    Name = var.name
  }
}

resource "aws_security_group" "jas_asg" {
  name = var.name_asg
  vpc_id = data.aws_vpc.jas.id
  ingress {
    protocol    = var.protocol
    from_port   = var.secure
    to_port     = var.secure
    cidr_blocks = ["${var.cidr_rt}"]
  }

  ingress {
    protocol    = var.protocol
    from_port   = var.bastion
    to_port     = var.bastion
    cidr_blocks = ["${var.cidr_rt}"]
  }

  ingress {
    protocol    = var.protocol
    from_port   = var.website
    to_port     = var.website
    cidr_blocks = ["${var.cidr_rt}"]
  }

  ingress {
    protocol    = var.icmp_protocol
    from_port   = var.icmp
    to_port     = var.egress
    cidr_blocks = ["${var.cidr_rt}"]
  }

  # all traffic allowed for egress
  egress {
    from_port   = var.egress
    to_port     = var.egress
    protocol    = var.protocol_egress
    cidr_blocks = ["${var.cidr_rt}"]
  }

  lifecycle {
    create_before_destroy = true
  }
  
  tags = {
    Name = var.name
  }
}

resource "aws_security_group" "jas_rds" {
  name = var.rds_identifier
  vpc_id = data.aws_vpc.jas.id

  # allow all external world traffic
  ingress {
    from_port   = var.rds
    to_port     = var.rds
    protocol    = var.protocol
    cidr_blocks = ["${var.cidr_rt}"]
  }

  # allow traffic from bastion host
  ingress {
    from_port   = var.bastion
    to_port     = var.bastion
    protocol    = var.protocol
    cidr_blocks = ["${var.cidr_rt}"]
  }

  # all traffic allowed for egress
  egress {
    from_port   = var.egress
    to_port     = var.egress
    protocol    = var.protocol_egress
    cidr_blocks = ["${var.cidr_rt}"]
  }

  lifecycle {
    create_before_destroy = true
  }
  
  tags = {
    Name = var.name
  }
}
