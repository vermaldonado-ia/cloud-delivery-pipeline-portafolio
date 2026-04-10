# 🚀 Cloud Delivery Pipeline Portafolio

![CI Pipeline](https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions/workflows/ci.yml/badge.svg)
![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=vermaldonado-ia_cloud-delivery-pipeline-portafolio\&metric=alert_status)
![Coverage](https://sonarcloud.io/api/project_badges/measure?project=vermaldonado-ia_cloud-delivery-pipeline-portafolio\&metric=coverage)

Repositorio orientado a demostrar la implementación de un pipeline de Integración Continua (CI) utilizando GitHub Actions, incorporando pruebas automatizadas, cobertura de código y análisis de calidad con SonarQube Cloud.

Este proyecto evidencia buenas prácticas de automatización y control de calidad en un flujo de desarrollo moderno, utilizando un ejemplo simple en Python.

---

## 🎯 Objetivo

Implementar un pipeline de CI que permita:

* Ejecutar pruebas automatizadas en cada cambio
* Medir cobertura de código
* Integrar análisis estático de calidad
* Validar estándares mediante Quality Gate
* Demostrar prácticas DevOps aplicadas a un proyecto Python

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

## 🧩 Flujo del pipeline

El pipeline implementado sigue una secuencia automatizada desde el cambio en el código hasta la validación de calidad:

```text
Developer Push / Pull Request
        ↓
GitHub Actions
        ↓
Instalación de dependencias
        ↓
Ejecución de lint (flake8)
        ↓
Formateo de código (black)
        ↓
Pruebas automatizadas (pytest)
        ↓
Generación de coverage.xml
        ↓
Análisis con SonarQube Cloud
        ↓
Validación de Quality Gate
```

Este flujo permite asegurar la calidad del código de forma automática antes de integrar cambios.

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

## ✅ Resultados logrados

Este pipeline permite:

* Ejecutar pruebas automáticamente en cada cambio del repositorio
* Detectar errores de forma temprana en el ciclo de desarrollo
* Medir cobertura de código de manera automatizada
* Validar estándares de calidad mediante SonarQube Quality Gate
* Asegurar la estabilidad del código antes de su integración
* Estandarizar el proceso de desarrollo mediante CI

Este enfoque mejora la confiabilidad del delivery y reduce riesgos en entornos productivos.

---

## 🧪 Validación de funcionamiento del pipeline

Para comprobar que el pipeline detecta errores de forma efectiva, se realizó una prueba controlada sobre la función `division` del proyecto.

### Escenario probado

Se introdujo intencionalmente una alteración en la lógica de la función para provocar un comportamiento incorrecto.

### Resultado observado

Al ejecutar el pipeline:

* Se corrieron 17 pruebas automatizadas
* 12 pruebas pasaron correctamente
* 5 pruebas fallaron en los casos asociados a la función `division`
* El job finalizó con `exit code 1`
* El pipeline detuvo la integración del cambio defectuoso

### Evidencia del fallo en el pipeline

![Pipeline Error](./docs/pipeline_error.png)

### Aprendizaje obtenido

Esta validación permitió comprobar que:

* El pipeline detecta errores funcionales de forma temprana
* Los tests automatizados protegen la lógica del código
* Un cambio incorrecto no avanza en el flujo de integración
* La cobertura de código no reemplaza la validación funcional

> Durante la prueba, la cobertura se mantuvo en 100%, pero los tests fallaron. Esto demuestra que una cobertura alta indica ejecución de código, pero no garantiza que la lógica sea correcta.

### Conclusión

El pipeline implementado no solo automatiza validaciones, sino que también actúa como mecanismo de control de calidad, evitando la integración de cambios defectuosos en el repositorio.

---

## 📁 Estructura del proyecto

```text
cloud-delivery-pipeline-portafolio/
├── .github/workflows/ci.yml
├── app_demo/
│   ├── src/
│   │   └── main.py
│   ├── tests/
│   │   └── test_main.py
│   └── requirements.txt
├── sonar-project.properties
├── docs/
│   ├── coverage.png
│   └── pipeline_error.png
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
* SonarQube Cloud

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

## ▶️ Ejecución local

Para ejecutar el proyecto y las pruebas en entorno local:

```bash
cd app_demo
pip install -r requirements.txt
PYTHONPATH=. pytest --cov=src --cov-report=xml --cov-report=term-missing tests
```

---

## 🔮 Próximos pasos

Como evolución del pipeline actual, se consideran las siguientes mejoras:

* Implementación de Continuous Deployment (CD) simulado
* Despliegue en entornos cloud (AWS / Azure)
* Integración con contenedores (Docker)
* Configuración de branch protection y control de calidad obligatorio
* Optimización del pipeline para entornos multi-stage

---

## 💡 Nota

Este proyecto fue desarrollado con fines demostrativos como parte de un portafolio profesional orientado a prácticas DevOps y Cloud.
