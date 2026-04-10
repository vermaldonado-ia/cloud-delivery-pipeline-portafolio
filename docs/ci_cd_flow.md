  # CI/CD Flow

## Flujo implementado en el repositorio

Este repositorio demuestra un flujo básico de CI/CD orientado a buenas prácticas DevOps.

### 1. Continuous Integration (CI)
El pipeline de CI ejecuta automáticamente:

- Instalación de dependencias
- Validación del entorno
- Linting del código
- Ejecución de pruebas automatizadas

### 2. Continuous Deployment (CD) Simulado
Una vez aprobada la validación del código, el flujo de CD simulado:

- Prepara una versión liberable de la aplicación
- Genera un log de despliegue
- Publica un artifact como evidencia del release

## Beneficios del enfoque

- Detección temprana de errores
- Automatización del control de calidad
- Estandarización del proceso de entrega
- Trazabilidad de cambios
- Base para una futura integración con despliegues reales en cloud
