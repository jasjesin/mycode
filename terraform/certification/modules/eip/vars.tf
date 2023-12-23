variable "location" {
  type = map
  default = {
      bucket = "jasjesin"
      key = "creds/terraform.tfstate"
      west = "us-west-1"
      east = "us-east-1"
      az1 = "us-west-1b"
      az2 = "us-west-1c"
  }
}