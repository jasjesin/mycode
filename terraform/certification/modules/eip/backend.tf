terraform {
  backend "s3" {
      bucket = "jasjesin"
      key = "creds/terraform.tfstate"
      region = "us-west-1"
      dynamodb_table = "tfstatelock"
  }
}
/*
resource "time_sleep" "delay" {
  create_duration = "200s"
}
*/
