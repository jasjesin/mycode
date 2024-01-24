variable "name" {
  description = "This value needs to be fetched from parent module"
}

variable "cidr_rt" {
  default = "0.0.0.0/0"
}

variable "default_route_table_id" {
  description = "This value needs to be fetched from parent module"
}

variable "igw_id" {
  description = "This value needs to be fetched from parent module"
}