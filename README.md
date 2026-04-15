# 🚀 Cloud Delivery Pipeline Portafolio

![CI](https://img.shields.io/badge/CI-GitHub%20Actions-orange?logo=githubactions)
![Coverage](https://img.shields.io/badge/Coverage-80%25%2B-success)
![CD](https://img.shields.io/badge/CD-AWS%20Amplify-blue?logo=amazonaws)
![Status](https://img.shields.io/badge/Status-Production-success)

🔗 **Producción:** https://main.d28beryienq64n.amplifyapp.com
🔗 **Repositorio:** https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio
🔗 **CI Pipeline:** https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions

---

## 💡 Descripción

Este proyecto demuestra la implementación de un pipeline DevOps completo, integrando prácticas de Integración Continua (CI), control de calidad y despliegue continuo (CD) real en la nube.

El objetivo es simular un flujo de entrega profesional utilizado en entornos empresariales.

---

## 🎯 Objetivo

Implementar un pipeline que permita:

* Detectar errores de forma temprana (Shift Left)
* Asegurar calidad del código antes del merge
* Validar cobertura de pruebas
* Controlar cambios hacia producción
* Automatizar despliegues en la nube

---

## ⚙️ Arquitectura del Pipeline

Flujo implementado:

Pull Request
↓
CI (GitHub Actions: Tests + Coverage + Quality Gate)
↓
Merge controlado a main
↓
CD automático (AWS Amplify)
↓
Producción disponible vía URL

---

## 🔄 Integración Continua (CI)

El pipeline ejecuta automáticamente:

* Instalación de dependencias
* Configuración de entorno Python
* Ejecución de pruebas con pytest
* Validación de cobertura con pytest-cov
* Bloqueo del merge si no se cumplen criterios

Esto permite garantizar la calidad antes de integrar cambios.

---

## 🧪 Quality Gate

Se implementa un Quality Gate basado en:

* Coverage mínimo requerido (ej: 80%)
* Validación de tests exitosos

Si no se cumplen las condiciones, el pipeline falla.

---

## 🚀 Continuous Deployment (CD)

El despliegue se realiza automáticamente mediante AWS Amplify:

* Detecta cambios en la rama main
* Ejecuta build automático
* Publica en entorno productivo

Esto permite un flujo de entrega completamente automatizado.

---

## 🧩 Caso de Uso Profesional (Enfoque Empresa)

En entornos corporativos, uno de los principales desafíos es asegurar la calidad del software antes de su liberación, evitando errores en producción y reduciendo retrabajo.

Este proyecto simula un escenario real donde:

* múltiples desarrolladores realizan cambios simultáneamente
* existe riesgo de introducir defectos en cada entrega
* se requiere control automatizado del flujo de cambios

Para abordar este problema, se implementa un pipeline DevOps que:

* valida automáticamente cada cambio mediante CI
* aplica un Quality Gate basado en cobertura de pruebas
* bloquea integraciones que no cumplen estándares
* automatiza el despliegue hacia un entorno productivo

Esto permite reducir riesgos, mejorar la calidad del código y acelerar la entrega continua.

---

## 🌐 Resultado

El sistema queda disponible en producción:

👉 https://main.d28beryienq64n.amplifyapp.com

---

## 👩‍💻 Sobre el proyecto

Este portafolio fue desarrollado con foco en demostrar capacidades en:

* DevOps
* Automatización de pipelines
* Integración de herramientas CI/CD
* Despliegue en la nube (AWS)

---

## 📌 Stack Tecnológico

* Python
* Pytest
* GitHub Actions
* AWS Amplify
* Git / GitHub

---

## 🏢 Aplicación en Experiencia Profesional

Este enfoque se alinea directamente con mi experiencia liderando proyectos en entornos como AFP y plataformas ERP.

En iniciativas de transformación digital, enfrenté desafíos como:

* múltiples versiones de plataformas en producción
* alta dependencia de validaciones manuales
* riesgo de errores en liberaciones
* necesidad de reducir tiempos de entrega

Este tipo de pipeline permite abordar estos problemas mediante:

* automatización de validaciones técnicas
* control de calidad previo al despliegue
* estandarización del flujo de entrega
* reducción de errores en producción

Particularmente en contextos como:

* modernización de plataformas ERP (ej: Importline)
* implementación de prácticas ágiles en AFP
* integración de equipos técnicos y de negocio

Este proyecto refleja cómo llevar esas prácticas a un enfoque DevOps moderno, combinando automatización, calidad y despliegue continuo en la nube.
