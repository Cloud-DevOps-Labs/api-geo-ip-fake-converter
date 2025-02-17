output "api_endpoint" {
  value = "${aws_apigatewayv2_api.lambda_api.api_endpoint}/coords"
}

output "api_key" {
  value = random_password.api_key.result
  sensitive = true
}

output "curl_example" {
  value = "curl '${aws_apigatewayv2_api.lambda_api.api_endpoint}/coords?ip=1.2.3.4&api_key=${random_password.api_key.result}'"
  sensitive = true
}
