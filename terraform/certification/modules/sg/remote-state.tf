data "terraform_remote_state" "eip" {
  backend = "s3" 
  config = {
      bucket = "jasjesin"
      key = "creds/terraform.tfstate"
      region = "us-west-1"
#      dynamodb_table = "tfstatelock"
  } 
}