resource "aws_instance" "node1" {
    ami = ""
    instance_type = "t3.micro"

    tags {
        Name = "control plane"
    }
}

resource "aws_instance" "node2" {
    ami = ""
    instance_type = "t3.micro"

    tags {
        Name = "worker1"
    }
}

resource "aws_instance" "node3" {
    ami = ""
    instance_type = "t3.micro"

    tags {
        Name = "worker2"
    }
}