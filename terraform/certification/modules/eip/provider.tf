provider "aws" {
  region = var.location.west
}
provider "aws" {
  alias = "awsterraform"
  profile = "terraform"
  region = var.location.east
}