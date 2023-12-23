resource "local_file" "jas" {
  filename = each.value
  for_each = var.filename
  content  = data.local_file.test.content
}

data "local_file" "test" {
  filename = "/Users/jasdil/Documents/Learnings/terraform/projects/for_loop_test/test1.txt"
}
