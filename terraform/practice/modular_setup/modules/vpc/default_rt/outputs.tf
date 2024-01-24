output "default_rt_id" {
  value = aws_default_route_table.default_rt.id
}

output "default_rt_vpc_id" {
  value = aws_default_route_table.default_rt.vpc_id
}

output "default_rt_route" {
  value = aws_default_route_table.default_rt.route
}