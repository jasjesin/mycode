
output "vpc_id" {
  value = aws_vpc.jas.id
}

output "ig_id" {
  value = aws_internet_gateway.jas.id
}

output "ig_vpc" {
  value = aws_internet_gateway.jas.vpc_id
}

output "rt_id" {
  value = aws_route_table.jas_public_blue.id
}

output "rt_vpc" {
  value = aws_route_table.jas_public_blue.vpc_id
}

output "public_blue_subnet_id" {
  value = aws_subnet.jas_public_blue.id
}

output "public_blue_subnet_vpc_id" {
  value = aws_subnet.jas_public_blue.id
}

output "public_subnet_rt_association_igw_id" {
  value = aws_route_table_association.jas_public_blue.id
}

output "pvt_subnet_blue_id" {
  value = aws_subnet.jas_pvt_blue.id
}

output "pvt_subnet_blue_vpc_id" {
  value = aws_subnet.jas_pvt_blue.vpc_id
}

output "pvt_subnet_blue_rt_id" {
  value = aws_route_table_association.jas_pvt_blue_nat_gw.id
}

output "pvt_subnet_blue_rt_association_igw_id" {
  value = aws_route_table_association.jas_pvt_blue_nat_gw.gateway_id
}

output "public_subnet_ids" {
  value = data.aws_subnets.public_jas.ids
}


output "sg_details" {
  value = aws_security_group.jas_ec2.id
}

output "current_region" {
  value = data.aws_region.current_region.name
}

output "ami_id" {
  value = data.aws_ami.app_ami.id
}