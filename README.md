# IP to Coordinates API

Servicio serverless que convierte direcciones IP en coordenadas GPS aleatorias (siempre en tierra firme). Implementado con AWS Lambda y API Gateway.

## Características

- Autenticación mediante API key
- Coordenadas aleatorias siempre en tierra firme (continentes)
- Serverless (AWS Lambda + API Gateway)
- Infraestructura como código (Terraform)

## Requisitos Previos

- AWS CLI configurado con credenciales
- Terraform instalado
- Python 3.9 o superior

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/ip-to-coords-api.git
cd ip-to-coords-api
```

2. (Opcional) Modifica las variables en `terraform/variables.tf`:
- `aws_region`: Región de AWS
- `api_key`: Clave de API personalizada

## Despliegue

1. Inicializa y aplica la configuración de Terraform:
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

2. Al finalizar, Terraform mostrará la URL de la API.

## Uso

La API acepta peticiones GET con los siguientes parámetros:

- `ip`: La dirección IP a convertir
- `api_key`: Clave de API para autenticación

### Ejemplo de Uso

```bash
curl "https://[tu-api-id].execute-api.[region].amazonaws.com/coords?ip=1.2.3.4&api_key=test-api-key-123"
```

### Respuesta

```json
{
    "ip": "1.2.3.4",
    "latitude": 45.123456,
    "longitude": -75.987654
}
```

## Estructura del Proyecto

```
.
├── src/
│   └── lambda_function.py    # Código de la función Lambda
├── terraform/
│   ├── main.tf              # Configuración principal de Terraform
│   ├── variables.tf         # Variables de Terraform
│   └── outputs.tf           # Outputs de Terraform
├── .gitignore
├── LICENSE.md
└── README.md
```

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.
