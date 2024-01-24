output "vpc_id" {
  value = module.vpc.vpc_id
}

output "igw_id" {
  value = module.vpc.igw_id
}

output "igw_vpc_id" {
  value = module.vpc.igw_vpc_id
}

output "default_rt_id" {
  value = module.vpc.default_rt_id
}

output "default_rt_vpc_id" {
  value = module.vpc.default_rt_vpc_id
}

/*
output "default_rt_route" {
  value = module.vpc.default_rt_route
}
*/