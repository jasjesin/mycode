variable "filename" {
  type = list(string)
  default = [
    "/Users/jasdil/Documents/Learnings/terraform/projects/local/app/jas.txt",
    "/Users/jasdil/Documents/Learnings/terraform/projects/local/app/jas1.txt",
    "/Users/jasdil/Documents/Learnings/terraform/projects/local/app/jas2.txt",
    "/Users/jasdil/Documents/Learnings/terraform/projects/local/test1.txt"
  ]
  description = "Path where file needs to be stored"
}

variable "file-content" {
  type = map(string)
  default = {
    "statement1" = "\n Statement1 \n"
    "statement2" = "\n Statement2 \n"
  }
  description = "What needs to be specified in the file"
}

variable "prefix" {
  type        = list(string)
  default     = ["Mr", "Mrs", "Sir"]
  description = "How should it be addressed"
}

variable "separator" {
  default     = ":"
  type        = string
  description = "Delimiting parameter"
}

variable "length" {
  default     = "1"
  type        = number
  description = "What should be the length"
}

variable "password_change" {
  default = true
  type    = bool
}

variable "bella" {
  type = object({
    name         = string
    color        = string
    age          = number
    food         = list(string)
    favorite_pet = bool
  })

  default = {
    age          = 7
    color        = "brown"
    favorite_pet = true
    food         = ["fish", "chicken", "turkey"]
    name         = "bella"
  }
}

variable "filename1" {
  type = set(string)
  default = [
    "abc",
    "def",
    "xyz"
  ]
  description = "Testing for loop"
}
