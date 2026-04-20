# 🚀 Cloud Delivery Pipeline Portafolio

💡 Caso práctico de implementación de un **pipeline DevOps end-to-end**, integrando validación continua, control de calidad y despliegue automático en la nube.

---

## 🌐 Producción

👉 URL del sitio desplegado:
https://main.d28beryienq64n.amplifyapp.com

El despliegue se realiza automáticamente en **AWS Amplify** tras cada cambio en la rama `main`.

---

## 🎯 Objetivo

Implementar un flujo de entrega que permita:

* Detectar errores de forma temprana (Shift Left)
* Asegurar calidad del código antes del merge
* Validar cobertura de pruebas
* Controlar cambios hacia producción
* Automatizar el despliegue en la nube

---

## 📐 Arquitectura del Pipeline

Flujo implementado:

Dev
↓
Pull Request
↓
CI (Tests + Coverage + Linting)
↓
Quality Gate
↓
Merge controlado a main
↓
CD (AWS Amplify)
↓
Producción

---

## 🧩 Enfoque de Arquitectura

Este proyecto implementa un enfoque **desacoplado**, separando claramente:

### 🧪 Validación Técnica (CI)

Ubicada en:

👉 `app_demo/`

Incluye:

* Aplicación Python de ejemplo
* Pruebas automatizadas con `pytest`
* Medición de cobertura (`pytest-cov`)
* Análisis de calidad con `flake8`
* Quality Gate (mínimo 80% coverage)

📌 Esta capa asegura calidad antes de permitir integración.

---

### 🌐 Despliegue Continuo (CD)

Ubicado en la raíz del proyecto:

👉 `index.html`

Incluye:

* Sitio estático desplegado en AWS Amplify
* Publicación automática tras merge a `main`
* URL accesible como evidencia del pipeline

📌 Representa la salida visible del flujo de entrega.

---

## 🔄 Integración Continua (CI)

El pipeline ejecuta automáticamente:

* Instalación de dependencias
* Configuración de entorno Python
* Ejecución de pruebas (`pytest`)
* Medición de cobertura
* Validación de calidad (`flake8`)

Si el Quality Gate falla:

⛔ Se detiene el pipeline
⛔ No se permite el merge

---

## 🛡️ Quality Gate

Implementación práctica inspirada en:

* SonarQube
* Azure DevOps Quality Gates

Validaciones:

✔ Tests exitosos
✔ Coverage ≥ 80%
✔ Sin errores de linting

---

## 🚀 Despliegue Continuo (CD)

El CD se activa cuando:

* Se realiza merge a la rama `main`

Acciones:

* Build del sitio estático
* Deploy automático en AWS Amplify
* Publicación en URL productiva

---

## 🔍 Evidencia del Pipeline

✔ Ejecución real en GitHub Actions
✔ Validación automática en cada cambio
✔ Despliegue automático en la nube

💡 Este flujo demuestra un pipeline donde cada cambio validado es desplegado automáticamente.

---

## 📊 Gestión del Delivery

Se incorpora trazabilidad del trabajo mediante:

* Backlog priorizado
* User Stories
* Story Points
* Tablero Kanban

👉 Ver detalle: `azure_devops/boards_evidencia.md`

📌 Esto conecta la gestión ágil con la ejecución técnica del pipeline.

---

## ⚠️ Alcance del Proyecto

* CI → Implementación real
* Quality Gate → Implementación práctica
* CD → Implementación real en AWS
* Gestión → Simulación con Azure DevOps

---

## 🧠 Enfoque de Delivery

Este proyecto demuestra cómo estructurar un flujo que:

* Minimiza riesgos antes del despliegue
* Asegura calidad continua
* Automatiza el ciclo de release
* Integra DevOps con gestión ágil

---

## 📚 Aprendizajes Clave

* Importancia del Quality Gate previo al merge
* Uso de métricas como coverage
* Automatización del flujo end-to-end
* Integración entre DevOps y Agile

---

## 🧱 Estructura del Repositorio

* `app_demo/` → Validación CI
* `.github/workflows/` → Pipeline
* `azure_devops/` → Gestión
* `docs/` → Evidencias
* `index.html` → Sitio desplegado

---

## 👩‍💼 Rol en este proyecto

Responsabilidades:

* Diseño del pipeline CI/CD
* Definición de Quality Gate
* Implementación con GitHub Actions
* Integración con AWS Amplify
* Trazabilidad con Azure DevOps

📌 Enfoque orientado a delivery y gobierno del flujo de entrega.

---

## 🚀 Conclusión

Este proyecto demuestra la capacidad de diseñar e implementar un pipeline DevOps completo, integrando calidad, automatización y despliegue continuo, alineado a prácticas utilizadas en entornos productivos.

---

## 🔗 Enlaces

👉 Repositorio:
https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio

👉 Pipeline (GitHub Actions):
https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions

👉 Demo en producción:
https://main.d28beryienq64n.amplifyapp.com

