variable "location" {
    type = map
    default = {
        region = "us-west-1"
        az1 = "us-west-1b"
        az2 = "us-west-1c"
    }
}
variable "team" {
  default = "jas"
}
variable "ports" {
    type = map
    default = {
        open = 0
        ssh = 22
        http = 80
        protocol = "tcp"
    }
}
variable "jas_ami" {
  type = map
  default  = {
      us-west-1 = "ami-00d8a762cb0c50254"
      instance_type = "t2.micro"
  }
}
variable "cidr_block" {
    type = map
    default = {
        outside = "0.0.0.0/0"
        vpc = "10.0.0.0/16"
        subnet1 = "10.0.1.0/24"
        subnet2 = "10.0.2.0/24"
    }
}
variable "keypair" {
    type = map
    default = {
    name = "us-region-key-pair"
    path = "/Users/jasdil/Documents/Learnings/terraform/creds/aws/us-region-key-pair.pub"
    }
}
