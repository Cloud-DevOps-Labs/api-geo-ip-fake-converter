variable "aws_region" {
  description = "AWS region for the resources"
  type        = string
  default     = "us-east-1"
}

variable "api_key" {
  description = "API Key for authentication"
  type        = string
  default     = "test-api-key-123"
}
