variable "filename" {
  type = set(string)
  default = [
    "/Users/jasdil/Documents/Learnings/terraform/projects/for_loop_test/app/jas.txt",
    "/Users/jasdil/Documents/Learnings/terraform/projects/for_loop_test/app/jas1.txt",
    "/Users/jasdil/Documents/Learnings/terraform/projects/for_loop_test/app/jas2.txt"
  ]
  description = "Path where file needs to be stored"
}
