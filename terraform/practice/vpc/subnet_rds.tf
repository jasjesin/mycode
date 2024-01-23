resource "aws_db_subnet_group" "jas" {
  name       = var.name_rds
  subnet_ids = data.aws_subnets.pvt_jas.ids
}