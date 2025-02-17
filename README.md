# IP to Coordinates API

API simple que convierte direcciones IP en coordenadas GPS aleatorias (siempre en tierra firme).

## Uso

La API acepta peticiones GET con los siguientes parámetros:

- `ip`: La dirección IP a convertir
- `api_key`: Clave de API para autenticación

Ejemplo de uso:

```bash
curl "https://[tu-api-id].execute-api.[region].amazonaws.com/coords?ip=1.2.3.4&api_key=test-api-key-123"
```

## Despliegue

1. Asegúrate de tener configuradas tus credenciales de AWS
2. Ejecuta:

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

3. La URL de la API se mostrará en los outputs de Terraform
