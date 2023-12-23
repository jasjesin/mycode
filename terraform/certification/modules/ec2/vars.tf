variable "location" {
  type = map
  default = {
      west = "us-west-1"
      east = "us-east-1"
      az1 = "us-west-1b"
      az2 = "us-west-1c"
  }
}
data "aws_ami" "ec2" {
  most_recent = true
  owners = ["amazon"]
  filter {
    name = "name"
    values = ["amzn2-ami-hvm*"]
  }
}
variable "ec2_ins_type" {
    type = map
    default = {
        default = "t2.nano"
        dev = "t2.micro"
        stage = "t2.micro"
        prd = "t2.large"
    }
  
}