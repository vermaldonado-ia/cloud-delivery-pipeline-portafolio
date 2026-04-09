# 🚀 Cloud Delivery Pipeline Portafolio

![CI Pipeline](https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions/workflows/ci.yml/badge.svg)

Repositorio que demuestra la implementación de un **pipeline de Integración Continua (CI)** utilizando **GitHub Actions**, enfocado en asegurar la calidad del código mediante automatización de validaciones, pruebas y métricas.

---

## 🎯 Objetivo

Implementar un pipeline CI que permita:

- Validar la calidad del código automáticamente  
- Detectar errores de forma temprana  
- Asegurar consistencia en el desarrollo  
- Establecer bases para prácticas DevOps y CI/CD  

---

## ⚙️ CI Pipeline

El pipeline está implementado con **GitHub Actions** y se ejecuta automáticamente en:

- Cada `push` a la rama `main`  
- Cada `pull request` hacia `main`  
- Ejecución manual (`workflow_dispatch`)  

### 🔍 Validaciones incluidas

- ✔ Instalación de dependencias  
- ✔ Validación del entorno Python (3.11)  
- ✔ Formato de código con **Black**  
- ✔ Análisis estático con **Flake8**  
- ✔ Ejecución de pruebas unitarias con **Pytest**  
- ✔ Medición de cobertura de código con **pytest-cov**  

---

## 🧪 Testing

El proyecto incluye pruebas unitarias que validan la lógica de negocio:

- Operaciones matemáticas básicas:
  - suma  
  - resta  
  - multiplicación  
  - división  
- Manejo de errores (división por cero)  
- Validación de casos borde:
  - valores negativos  
  - uso de cero  
  - resultados esperados  

Las pruebas se ejecutan automáticamente en el pipeline, asegurando la estabilidad del código en cada cambio.

---

## 📊 Cobertura de Código

Se implementa medición de cobertura para evaluar qué porcentaje del código es validado por pruebas.

Esto permite:

- Identificar código no testeado  
- Reducir riesgos en cambios futuros  
- Mejorar la calidad general del software  

📌 Cobertura actual del proyecto:

**100%**

![Coverage](./docs/coverage.png)

---

## 🏗️ Estructura del proyecto

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
│   └── coverage.png
├── sonarqube/
└── README.md
