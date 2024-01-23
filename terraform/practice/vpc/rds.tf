resource "aws_db_instance" "jas" {
  identifier                  = var.rds_identifier
  allocated_storage           = var.rds_storage
  engine                      = var.rds_engine
  instance_class              = var.rds_instance_class
  manage_master_user_password = var.manage_master_user_password
  db_name                     = var.rds_name
  username                    = var.rds_user
  db_subnet_group_name        = aws_db_subnet_group.jas.id
  vpc_security_group_ids      = ["${aws_security_group.jas_rds.id}"]
  skip_final_snapshot         = var.skip_final_snapshot
  final_snapshot_identifier   = var.final_snapshot_identifier

  lifecycle {
    create_before_destroy = true
  }
  
  tags = {
    Name = var.name
  }

}