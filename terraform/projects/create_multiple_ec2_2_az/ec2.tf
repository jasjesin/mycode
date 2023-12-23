resource "aws_instance" "jas_ec2_ins1" {
    ami = var.jas_ami[var.location.region]
    instance_type = var.jas_ami.instance_type
    subnet_id = aws_subnet.jas_public_subnet1.id
    vpc_security_group_ids = [aws_security_group.jas_sg1.id]
    key_name = aws_key_pair.jas_ec2_keypair.id
    count = 2
  tags = {
    "Name" = var.team
  }
}
resource "aws_instance" "jas_ec2_ins2" {
    ami = var.jas_ami[var.location.region]
    instance_type = var.jas_ami.instance_type
    subnet_id = aws_subnet.jas_public_subnet2.id
    vpc_security_group_ids = [aws_security_group.jas_sg1.id]
    key_name = aws_key_pair.jas_ec2_keypair.id
    count = 3
  tags = {
    "Name" = var.team
  }
}
resource "aws_key_pair" "jas_ec2_keypair" {
    key_name = var.keypair.name
    public_key = "${file(var.keypair.path)}"
}