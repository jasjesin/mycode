variable "instance_type" {
  default = "t2.micro"
}

variable "region" {
  default = "us-west-1"
}

variable "cidr_blocks" {
    type = list(string)
  default = [
      "10.0.0.0/16",
      "10.0.0.0/24",
      "0.0.0.0/0",
      "::/0"
  ]

}

variable "webserver" {
  default = "Webserver"
}

variable "environment" {
  default = "Production"
}

variable "aws_ami" {
    default = "amzn2-ami-hvm-*-x86_64-ebs"
  }
