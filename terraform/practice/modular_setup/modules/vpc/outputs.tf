output "vpc_id" {
  value = aws_vpc.vpc.id
}

output "igw_id" {
  value = module.igw.igw_id
}

output "igw_vpc_id" {
  value = module.igw.igw_vpc_id
}

output "default_rt_id" {
  value = module.default_rt.default_rt_id
}

output "default_rt_vpc_id" {
  value = module.default_rt.default_rt_vpc_id
}

output "default_rt_route" {
  value = module.default_rt.default_rt_route
}
