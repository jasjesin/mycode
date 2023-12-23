resource "aws_security_group" "sg1" {
/*  ingress {
#    cidr_blocks = [ "${aws_eip.eip1.public_ip}/32" ]
    cidr_blocks = [ "0.0.0.0/0" ]
    from_port = var.ports.http
    protocol = var.ports.protocol
    to_port = var.ports.http
  }
*/

  ingress {
    from_port   = local.ssh
    to_port     = local.ssh
    protocol    = local.protocol
    cidr_blocks = [var.ingress_cidr]
  }

  ingress {
    from_port   = local.https
    to_port     = local.https
    protocol    = local.protocol
 #   cidr_blocks = ["${data.terraform_remote_state.eip.outputs.eip1}/32"] #<-- pulls IP as output from eip.tf
    cidr_blocks = ["54.151.54.153/32"]
  }

  egress {
    from_port       = local.all
    to_port         = local.ephemeral
    protocol        = local.protocol
    cidr_blocks     = [local.cidr_all]  
  }  
    tags = {
    "Name" = var.name
  }
}

locals {
  http = 80
  https = 443
  ssh = 22
  all = 0
  ephemeral = 65535
  cidr_all = "0.0.0.0/0"
  protocol = "tcp"
}