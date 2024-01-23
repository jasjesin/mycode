resource "aws_db_parameter_group" "jas" {
  name   = var.name_rds
  family = var.rds_family
  parameter {
    name  = var.rds_charset_svr_name
    value = var.rds_charset_svr_value
  }
  parameter {
    name  = var.rds_charset_client_name
    value = var.rds_charset_client_value
  }
}