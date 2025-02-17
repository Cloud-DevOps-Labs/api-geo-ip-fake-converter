output "api_endpoint" {
  value = "${aws_apigatewayv2_api.lambda_api.api_endpoint}/coords"
}
