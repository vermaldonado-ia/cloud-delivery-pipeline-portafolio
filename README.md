# 🚀 Cloud Delivery Pipeline Portafolio

![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=vermaldonado-ia_cloud-delivery-pipeline-portafolio&metric=alert_status)

![Coverage](https://sonarcloud.io/api/project_badges/measure?project=vermaldonado-ia_cloud-delivery-pipeline-portafolio&metric=coverage)

Repositorio que demuestra la implementación de un **pipeline de Integración Continua (CI)** utilizando **GitHub Actions**, enfocado en asegurar la calidad del código mediante automatización de validaciones, pruebas y métricas.

---

## 🎯 Objetivo

Implementar un pipeline CI que permita:

* Validar la calidad del código automáticamente
* Detectar errores de forma temprana
* Asegurar consistencia en el desarrollo
* Establecer bases para prácticas DevOps y CI/CD

---

## ⚙️ Estrategia de Integración Continua

El pipeline está implementado con GitHub Actions y se ejecuta automáticamente en cada cambio relevante del repositorio.

Se implementa un pipeline CI orientado a:

* Asegurar calidad de código desde etapas tempranas
* Reducir defectos en producción
* Estandarizar el proceso de desarrollo
* Mejorar la confiabilidad del delivery

El pipeline automatiza validaciones técnicas como:

* Pruebas automatizadas (pytest)
* Análisis estático de código (flake8)
* Formateo de código (black)
* Medición de cobertura (pytest-cov)

---

## 🧪 Testing

El proyecto incluye pruebas unitarias que validan la lógica de negocio:

* Operaciones matemáticas básicas:

  * suma
  * resta
  * multiplicación
  * división
* Manejo de errores (división por cero)
* Validación de casos borde:

  * valores negativos
  * uso de cero
  * resultados esperados

Las pruebas se ejecutan automáticamente en el pipeline, asegurando la estabilidad del código en cada cambio.

---

## 📊 Cobertura de Código

Se implementa medición de cobertura para evaluar qué porcentaje del código es validado por pruebas.

Esto permite:

* Identificar código no testeado
* Reducir riesgos en cambios futuros
* Mejorar la calidad general del software

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
```

---

## 🚀 Tecnologías utilizadas

* Python 3.11
* Pytest
* Pytest-cov
* Flake8
* Black
* GitHub Actions

---

## 📈 Valor del proyecto

Este repositorio demuestra capacidades en:

* Automatización de pipelines CI
* Integración de pruebas automatizadas
* Control de calidad de código
* Uso de métricas de cobertura
* Buenas prácticas de desarrollo

👉 Enfocado en roles de **Cloud & DevOps Delivery / Engineering**

---

## 🔮 Próximos pasos

* Integración con SonarQube
* Incorporación de Continuous Deployment (CD)
* Despliegue en entornos cloud (AWS / Azure)
* Integración con contenedores (Docker)

---

## 💡 Nota

Este proyecto fue desarrollado con fines demostrativos como parte de un portafolio profesional orientado a prácticas DevOps y Cloud.
