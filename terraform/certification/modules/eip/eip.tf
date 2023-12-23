resource "aws_eip" "eip1" {
  vpc = true
}
output "eip1" {
    value = aws_eip.eip1.public_ip
  
}

resource "aws_eip" "eip2" {
  vpc = true
  provider = aws.awsterraform
}
output "eip2" {
    value = aws_eip.eip2.public_ip
  
}
