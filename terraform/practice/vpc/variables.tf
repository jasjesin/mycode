variable "cidr_block" {
  default = "10.0.0.0/16"
}

variable "cidr_rt" {
  default = "0.0.0.0/0"
}

variable "cidr_public_green_subnet" {
  default = "10.0.0.0/18"
}

variable "cidr_public_blue_subnet" {
  default = "10.0.64.0/18"
}

variable "cidr_pvt_blue_subnet" {
  default = "10.0.128.0/18"
}

variable "cidr_pvt_green_subnet" {
  default = "10.0.192.0/18"
}

variable "region" {
  default = "us-east-1"
}


variable "availability_zone_blue" {
  default = "us-east-1a"
}

variable "availability_zone_green" {
  default = "us-east-1b"
}

variable "map_public_ip_on_launch" {
  default = "true"
}

/*
variable "map_public_ip_on_launch" {
  default = "${var.cidr_public_subnet == "10.0.0.0/18" ? true : false}"
}
*/

variable "instance_tenancy" {
  default = "default"
}

variable "enable_dns_hostnames" {
  default = "true"
}

variable "enable_dns_support" {
  default = "true"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "protocol" {
  default = "tcp"
}

variable "protocol_egress" {
  default = "-1"
}

variable "ingress_22" {
  default = "allow"
}

variable "ingress_80" {
  default = "allow"
}

variable "egress" {
  default = "0"
}

variable "icmp" {
  default = "8"
}

variable "bastion" {
  default = "22"
}

variable "website" {
  default = "80"
}

variable "rds" {
  default = "3306"
}

variable "ephemeral_from" {
  default = "1024"
}

variable "ephemeral_to" {
  default = "65535"
}

variable "name" {
  default = "jas"
}

variable "name_elb" {
  default = "jas-elb"
}

variable "name_ec2" {
  default = "jas-ec2"
}

variable "name_asg" {
  default = "jas-asg"
}

variable "name_rds" {
  default = "jas-rds"
}

variable "name_public_blue" {
  default = "jas_public_blue"
}

variable "name_public_green" {
  default = "jas_public_green"
}

variable "name_pvt_blue" {
  default = "jas_pvt_blue"
}

variable "name_pvt_green" {
  default = "jas_pvt_green"
}

variable "users" {
  default = ["Waheguru", "pls", "get", "me", "stable", "job", "fast"]
  type    = list(string)
}

variable "group" {
  default = "dev"
}

variable "policy_name" {
  default = "developers"
}

variable "secure" {
  default = "443"
}

variable "http_protocol" {
  default = "HTTP"
}

variable "icmp_protocol" {
  default = "icmp"
}

variable "tg_type" {
  default = "instance"
}

variable "listener_type" {
  default = "forward"
}

variable "stickiness" {
  default = "true"
}

variable "stickiness_duration" {
  default = "28800"
}

variable "ami" {
  default = "ami-0c0b74d29acd0cd97"
}

variable "associate_public_ip_address" {
  default = "true"
}

variable "min" {
  default = 2
}

variable "max" {
  default = 3
}

variable "key" {
  default = "Name"
}

variable "rds_family" {
  default = "mysql5.6"
}

variable "rds_charset_svr_name" {
  default = "character_set_server"
}

variable "rds_charset_svr_value" {
  default = "utf8"
}

variable "rds_charset_client_name" {
  default = "character_set_client"
}

variable "rds_charset_client_value" {
  default = "utf8"
}

variable "rds_identifier" {
  default = "jas-mysql"
}

variable "rds_storage" {
  default = "5"
}

variable "rds_engine" {
  default = "mysql"
}

variable "rds_instance_class" {
  default = "db.t2.micro"
}

variable "manage_master_user_password" {
  default = "true"
}

variable "rds_name" {
  default = "jas"
}

variable "rds_user" {
  default = "jas"
}

variable "skip_final_snapshot" {
  default = "true"
}

variable "final_snapshot_identifier" {
  default = "ignore"
}