provider "aws" {
  region = var.aws_region
}

# Generate random API key
resource "random_password" "api_key" {
  length  = 32
  special = false
  override_special = "!@#$%&*()-_=+[]{}<>:?"
  upper   = true
  lower   = true
  numeric = true
}

# ZIP del código Lambda
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/../src/lambda_function.py"
  output_path = "${path.module}/lambda_function.zip"
}

# Rol IAM para Lambda
resource "aws_iam_role" "lambda_role" {
  name = "ip_to_coords_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# Política básica de logs para Lambda
resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Función Lambda
resource "aws_lambda_function" "ip_to_coords" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = "ip_to_coords"
  role            = aws_iam_role.lambda_role.arn
  handler         = "lambda_function.lambda_handler"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  runtime         = "python3.9"

  environment {
    variables = {
      API_KEY = random_password.api_key.result
    }
  }
}

# API Gateway
resource "aws_apigatewayv2_api" "lambda_api" {
  name          = "ip-to-coords-api"
  protocol_type = "HTTP"
}

# Etapa por defecto para API Gateway
resource "aws_apigatewayv2_stage" "lambda_stage" {
  api_id = aws_apigatewayv2_api.lambda_api.id
  name   = "$default"
  auto_deploy = true
}

# Integración de API Gateway con Lambda
resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id           = aws_apigatewayv2_api.lambda_api.id
  integration_type = "AWS_PROXY"

  integration_uri    = aws_lambda_function.ip_to_coords.invoke_arn
  integration_method = "POST"
}

# Ruta GET para la API
resource "aws_apigatewayv2_route" "get_coords" {
  api_id    = aws_apigatewayv2_api.lambda_api.id
  route_key = "GET /coords"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

# Permiso para que API Gateway invoque Lambda
resource "aws_lambda_permission" "api_gw" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ip_to_coords.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.lambda_api.execution_arn}/*/*"
}
