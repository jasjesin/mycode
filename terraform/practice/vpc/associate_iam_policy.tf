resource "aws_iam_group_policy_attachment" "jas" {
  group      = aws_iam_group.jas.name
  policy_arn = aws_iam_policy.jas.arn
}