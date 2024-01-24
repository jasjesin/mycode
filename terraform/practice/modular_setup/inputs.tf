variable "name" {
  description = "This is a mandatory input"
}

variable "region" {
  default = "This is a mandatory input"
}

variable "cidr_block" {
  description = "This is a mandatory input"
}

variable "instance_tenancy" {
  description = "This is an optional input"
}

variable "enable_dns_hostnames" {
  description = "This is an optional input"
}

variable "enable_dns_support" {
  description = "This is an optional input"
}

