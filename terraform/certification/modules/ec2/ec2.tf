resource "aws_instance" "ec2_ins1" {
  ami = data.aws_ami.ec2.id
  instance_type = lookup(var.ec2_ins_type,terraform.workspace)
  key_name = var.keypair.newname    #<-- this should be same keyname as generated from console n present under key pairs
  vpc_security_group_ids = [aws_security_group.sg1.id]
#  count = var.Prod == "yes" ? 1 : 0
  tags = local.common_tags
/*  tags = {
    "Name" = var.ec2_names[count.index]
  }
*/
# Code for provisioner to setup nginx webserver
/*  provisioner "local-exec" {
    command = "echo ${aws_instance.ec2_ins1.private_ip} >> pvt_ip.txt"
  }
  provisioner "local-exec" {
    when = destroy
    command = "rm pvt_ip.txt"  
  }
*/
/*
provisioner "remote-exec" {
  inline = [
    "sudo amazon-linux-extras install -y nginx1",
    "sudo systemctl start nginx"
  ]
  connection {
    type = "ssh"
    host = self.public_ip
    user = "ec2_user"
#    private_key = "${file("./creds/terraform_ec2_keypair.pem")}"
    private_key = "${file("./${var.keypair.pem}")}"
  }
}
*/
}
