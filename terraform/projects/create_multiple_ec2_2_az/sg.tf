resource "aws_security_group" "jas_sg1" {
  vpc_id = aws_vpc.jas_vpc1.id
  
  egress {
    cidr_blocks = [var.cidr_block.outside]
    from_port = var.ports.open
    to_port = var.ports.open
    protocol = -1
  }

  ingress {
    cidr_blocks = [var.cidr_block.outside]
    from_port = var.ports.ssh
    to_port = var.ports.ssh
    protocol = var.ports.protocol
  }
  
  ingress {
    cidr_blocks = [var.cidr_block.outside]
    from_port = var.ports.http
    to_port = var.ports.http
    protocol = var.ports.protocol
  }

  tags = {
    "Name" = var.team
  }
}