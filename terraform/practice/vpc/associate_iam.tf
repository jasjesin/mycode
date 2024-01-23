
resource "aws_iam_user_group_membership" "jas" {
  count  = length(var.users)
  user   = element(var.users, count.index)
  groups = [aws_iam_group.jas.name]
}