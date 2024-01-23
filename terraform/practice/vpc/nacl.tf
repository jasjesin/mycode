
resource "aws_network_acl" "jas_blue" {
  vpc_id     = data.aws_vpc.jas.id
  subnet_ids = [data.aws_subnet.jas_public_blue.id]

  # allow ingress for bastion host from port 22
  ingress {
    protocol   = var.protocol
    rule_no    = 100
    action     = var.ingress_22
    cidr_block = data.aws_subnet.jas_public_blue.cidr_block
    from_port  = var.bastion
    to_port    = var.bastion
  }

  # allow ingress for website traffic from port 80
  ingress {
    protocol   = var.protocol
    rule_no    = 200
    action     = var.ingress_80
    cidr_block = data.aws_subnet.jas_public_blue.cidr_block
    from_port  = var.website
    to_port    = var.website
  }

  # allow ingress for ephemeral ports
  ingress {
    protocol   = var.protocol
    rule_no    = 300
    action     = var.ingress_80
    cidr_block = data.aws_subnet.jas_public_blue.cidr_block
    from_port  = var.ephemeral_from
    to_port    = var.ephemeral_to
  }

  # allow egress to bastion at port 22
  ingress {
    protocol   = var.protocol
    rule_no    = 100
    action     = var.ingress_22
    cidr_block = data.aws_subnet.jas_public_blue.cidr_block
    from_port  = var.bastion
    to_port    = var.bastion
  }

  tags = {
    Name = var.name
  }
}


resource "aws_network_acl" "jas_green" {
  vpc_id     = data.aws_vpc.jas.id
  subnet_ids = [data.aws_subnet.jas_public_green.id]

  # allow ingress for bastion host from port 22
  ingress {
    protocol   = var.protocol
    rule_no    = 100
    action     = var.ingress_22
    cidr_block = data.aws_subnet.jas_public_green.cidr_block
    from_port  = var.bastion
    to_port    = var.bastion
  }

  # allow ingress for website traffic from port 80
  ingress {
    protocol   = var.protocol
    rule_no    = 200
    action     = var.ingress_80
    cidr_block = data.aws_subnet.jas_public_green.cidr_block
    from_port  = var.website
    to_port    = var.website
  }

  # allow ingress for ephemeral ports
  ingress {
    protocol   = var.protocol
    rule_no    = 300
    action     = var.ingress_80
    cidr_block = data.aws_subnet.jas_public_green.cidr_block
    from_port  = var.ephemeral_from
    to_port    = var.ephemeral_to
  }

  # allow egress to bastion at port 22
  ingress {
    protocol   = var.protocol
    rule_no    = 100
    action     = var.ingress_22
    cidr_block = data.aws_subnet.jas_public_green.cidr_block
    from_port  = var.bastion
    to_port    = var.bastion
  }

  tags = {
    Name = var.name
  }
}
