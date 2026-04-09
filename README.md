![CI Pipeline](https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions/workflows/ci.yml/badge.svg)

## CI Pipeline

Este repositorio incluye un pipeline de Integración Continua con GitHub Actions que ejecuta automáticamente:

- Instalación de dependencias
- Validación del entorno Python
- Ejecución de pruebas automatizadas con pytest

El pipeline se activa en cada push y pull request hacia la rama principal.

## Estructura del proyecto

```text
cloud-delivery-pipeline-portafolio/
├── .github/workflows/ci.yml
├── app_demo/
│   ├── src/
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
├── aws/
├── azure_devops/
├── docs/
├── sonarqube/
└── README.md
