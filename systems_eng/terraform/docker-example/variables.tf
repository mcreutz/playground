# This file is used to define variables that can be passed to the module

variable "port" {
  description = "Host port that is mapped to the container port"
  type        = number
  default     = 8003
}