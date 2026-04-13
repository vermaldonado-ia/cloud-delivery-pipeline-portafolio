# 🚀 Cloud Delivery Pipeline Portafolio

![CI Pipeline](https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-green)
![Coverage](https://img.shields.io/badge/Coverage-Enforced-orange)

Repositorio orientado a demostrar la implementación de un **pipeline de Integración Continua (CI)** y bases de **Continuous Delivery/Deployment (CD)** utilizando **GitHub Actions**, con foco en calidad de código, pruebas automatizadas y control de cobertura.

---

## 🎯 Objetivo

Construir un portafolio práctico que evidencie la implementación de un pipeline moderno de entrega de software, permitiendo:

- Validar calidad de código automáticamente
- Detectar errores tempranamente
- Ejecutar pruebas automatizadas en cada cambio
- Exigir cobertura mínima antes de integrar cambios
- Establecer un **Quality Gate** dentro del pipeline
- Sentar bases para evolucionar hacia un flujo CI/CD más completo

---

## 🧩 Alcance del repositorio

Este repositorio representa una implementación progresiva de prácticas DevOps aplicadas a un proyecto demostrativo en Python.

Actualmente incluye:

- **CI automatizado con GitHub Actions**
- **Linting y validación de calidad**
- **Pruebas automatizadas con pytest**
- **Control de cobertura**
- **Estructura preparada para Code Quality**
- **Base para despliegue continuo (CD)**

---

## ⚙️ Pipeline implementado

El pipeline de CI se ejecuta automáticamente en:

- `push` a la rama principal
- `pull request`

### Flujo general

```text
Push / Pull Request
        ↓
Instalación de dependencias
        ↓
Validación de estilo / calidad
        ↓
Ejecución de pruebas automatizadas
        ↓
Medición de cobertura
        ↓
Quality Gate
        ↓
Aprobación del pipeline

---

🛠️ Tecnologías utilizadas
Python 3.11
GitHub Actions
Pytest
Pytest-cov
Flake8
Markdown
SonarQube (estructura de integración y configuración)

---

📁 Estructura del proyecto

cloud-delivery-pipeline-portafolio/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── cd.yml
│       └── ci_cd.yml
├── app_demo/
│   ├── src/
│   │   └── main.py
│   ├── tests/
│   │   └── test_main.py
│   ├── README.md
│   └── requirements.txt
├── aws/
├── azure_devops/
├── docs/
├── sonarqube/
├── README.md
├── sonar-project.properties
└── trigger.txt

---

✅ Qué valida este pipeline
El pipeline está diseñado para asegurar criterios mínimos de calidad antes de aceptar cambios en el repositorio.
Valida:
Instalación correcta de dependencias
Ejecución sin errores del proyecto
Pruebas automatizadas exitosas
Cumplimiento de cobertura mínima
Reglas de calidad y consistencia del código

---

🧪 Evidencias del pipeline
A continuación se documentan distintos escenarios de ejecución del pipeline para demostrar su comportamiento.
1. Pipeline exitoso
Evidencia de ejecución correcta del flujo CI cuando el código cumple con pruebas, calidad y cobertura.

![CI Success](docs/ci-success.png)

2. Falla por pruebas
Ejemplo de pipeline fallando cuando una prueba automatizada no cumple el resultado esperado.

![Test Fail](docs/test-fail.png)

3. Falla por cobertura
Ejemplo de pipeline fallando cuando la cobertura no alcanza el umbral definido.

![Coverage Fail](docs/coverage-fail.png)

---

📌 Quality Gate implementado
Dentro del pipeline se aplican controles que funcionan como un Quality Gate, evitando integrar cambios que no cumplan condiciones mínimas de calidad.

Esto permite:
Reducir defectos
Detectar regresiones
Mantener estándares de desarrollo
Aumentar confiabilidad del flujo de entrega

---

🔍 Módulo de Code Quality
El repositorio incorpora una carpeta sonarqube/ para documentar y estructurar el componente de análisis de calidad de código.
Este módulo complementa el pipeline CI con una visión orientada a:
mantenibilidad
revisión técnica
validación estructural del código
expansión futura hacia un análisis más avanzado
📎 Más detalle en:

sonarqube/README.md

---

🚀 Valor del proyecto dentro del portafolio
Este repositorio me permite demostrar de forma práctica competencias asociadas a:
Integración Continua
Automatización de validaciones
Control de calidad en el ciclo de desarrollo
DevOps Foundations
Uso de GitHub Actions en entornos reales de portafolio
Diseño de pipelines orientados a confiabilidad

---

📈 Próximos pasos
La evolución natural de este repositorio considera:
incorporar una etapa de despliegue más completa
agregar validaciones adicionales de calidad
ampliar el proyecto demo
robustecer el módulo de Code Quality
integrar más evidencia visual del pipeline

---

👩‍💻 Autora
Verónica Maldonado Céspedes
Ingeniera Civil Informática | Project Manager | Scrum Master | Cloud & DevOps Delivery Manager
Este repositorio forma parte de mi proceso de reinvención profesional hacia roles vinculados a Cloud, DevOps, Delivery y Transformación Tecnológica.

---

🔗 Repositorios relacionados
Este proyecto complementa otros repositorios de mi portafolio profesional, orientados a:
transformación ágil
liderazgo de equipos
métricas y mejora continua
delivery en contextos cloud

⭐ Nota final
Este repositorio no busca solo mostrar teoría, sino una implementación práctica y visible de controles de calidad dentro de un pipeline automatizado, reflejando una base sólida para evolucionar hacia prácticas DevOps más robustas.
