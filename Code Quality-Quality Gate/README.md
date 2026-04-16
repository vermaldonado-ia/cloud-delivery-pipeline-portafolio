# 🔍 Code Quality - Quality Gate

![CI Pipeline](https://github.com/vermaldonado-ia/cloud-delivery-pipeline-portafolio/actions/workflows/ci.yml/badge.svg)

Este módulo implementa un **Quality Gate dentro de un pipeline CI/CD**, asegurando que solo código que cumple estándares de calidad pueda avanzar hacia etapas de despliegue.

Se inspira en herramientas como **SonarQube** y **Azure DevOps Quality Gates**, pero está implementado de forma práctica utilizando **GitHub Actions**.

---

## 🎯 Objetivo

Implementar un mecanismo automático que permita:

* Detectar errores de forma temprana (Shift Left)
* Validar estándares de desarrollo
* Controlar cobertura de pruebas
* Bloquear cambios defectuosos antes del despliegue

---

## ⚙️ Rol dentro del Pipeline

El Quality Gate actúa como una etapa intermedia crítica:

```
Pull Request / Push
        ↓
CI (Tests + Coverage)
        ↓
Code Quality (Quality Gate)
        ↓
Merge controlado a main
        ↓
CD (Deploy simulado)
```

Este punto define si el código puede o no avanzar en el flujo de entrega.

---

## 🛠️ Herramientas utilizadas

* flake8 → análisis estático de código (linting)
* pytest → ejecución de pruebas
* pytest-cov → medición de cobertura

---

## 🚫 Reglas de calidad implementadas

El pipeline falla automáticamente si:

* ❌ Existen errores de linting
* ❌ Algún test falla
* ❌ La cobertura es menor al mínimo definido

Esto asegura que ningún código defectuoso llegue a producción.

---

## 🧪 Implementación del Quality Gate

El control se ejecuta dentro del pipeline CI mediante:

* Validación de estilo de código
* Ejecución de pruebas automatizadas
* Evaluación de cobertura

Ejemplo de ejecución:

```
pytest --cov=src --cov-fail-under=80
flake8 .
```

Si alguna condición falla, el pipeline se detiene automáticamente.

---

## ❌ Evidencia: Falla por pruebas

Se introdujo un error intencional en el código para validar el comportamiento del pipeline.

**Resultado:**

* El pipeline falla correctamente
* Se bloquea el avance a etapas posteriores
* Se evita integración de código defectuoso

---

## 📊 Evidencia: Falla por cobertura

Se configuró un umbral mínimo de cobertura, provocando una falla controlada.

**Resultado:**

* Se exige cobertura mínima obligatoria
* Se asegura calidad estructural del código
* Se refuerza disciplina de testing

---

## 📊 Resultado actual

* ✅ Coverage: 100%
* ✅ Quality Gate aprobado
* ✅ Pipeline exitoso

---

## 🧠 Quality Gate Simulado

Este enfoque replica el comportamiento de herramientas como:

* SonarQube
* Azure DevOps Quality Gates

Aunque no se utiliza una herramienta externa, el pipeline cumple el mismo propósito:

* Validar calidad automáticamente
* Bloquear despliegue si no se cumplen estándares
* Reducir deuda técnica

---

## 🚀 Valor DevOps

Este módulo permite:

* Aplicar Shift Left Testing
* Automatizar controles de calidad
* Asegurar estándares antes de producción
* Mejorar confiabilidad del software

---

## 📈 Impacto en el flujo de entrega

Gracias al Quality Gate:

* Se reduce el riesgo en producción
* Se mejora la confiabilidad del pipeline
* Se estandariza la calidad del código
* Se controla el flujo de cambios

---

## 📌 Conclusión

El Quality Gate implementado garantiza que:

* Solo código validado avanza en el pipeline
* Se mantienen estándares de desarrollo
* Se reduce el riesgo en despliegues

Este enfoque es clave en entornos DevOps modernos.

---

## 🔗 Relación con el proyecto

Este módulo forma parte del repositorio principal:

👉 Cloud Delivery Pipeline Portafolio

Donde se integra con:

* CI Pipeline
* Control de Pull Request
* CD Simulado
