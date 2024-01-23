resource "aws_iam_user" "jas" {
  count = length(var.users)
  name  = element(var.users, count.index)
}