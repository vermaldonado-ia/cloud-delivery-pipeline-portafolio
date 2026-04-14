# 🔍 Code Quality - Quality Gate

![Code Quality](https://img.shields.io/badge/Quality-Gate%20Implemented-blue)  
![Linting](https://img.shields.io/badge/Linting-Flake8-blueviolet)  
![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen)

Este módulo representa la implementación de un **Quality Gate dentro del pipeline CI/CD**, enfocado en asegurar la calidad del código antes del despliegue.

Se basa en prácticas utilizadas en herramientas como SonarQube, pero implementado de forma simplificada dentro de GitHub Actions.

---

## 🎯 Objetivo

Asegurar estándares mínimos de calidad mediante:

- detección temprana de errores  
- validación de buenas prácticas  
- control de cobertura de pruebas  
- bloqueo automático del pipeline  

---

## ⚙️ Rol dentro del pipeline

Flujo conceptual:

CI (Tests + Coverage)  
↓  
Code Quality (Quality Gate)  
↓  
CD (Deploy)  

Este módulo actúa como un **punto de control obligatorio** antes del despliegue.

---

## 🛠️ Herramientas utilizadas

- **flake8** → análisis estático de código (linting)  
- **pytest** → ejecución de pruebas  
- **pytest-cov** → medición de cobertura  

---

## 🚫 Reglas de calidad implementadas

El pipeline falla automáticamente si:

- existen errores de linting  
- los tests fallan  
- la cobertura no cumple el mínimo definido  

Esto permite evitar que código defectuoso avance en el flujo CI/CD.

---

## ❌ Evidencia: Falla por pruebas

Se modificó el código intencionalmente para generar una falla en los tests, validando el comportamiento del pipeline.

![Test Fail](../docs/test-fail.png)

Resultado:
- el pipeline se detiene correctamente  
- se evita el avance a siguientes etapas  

---

## 📊 Evidencia: Falla por cobertura

Se configuró un umbral mínimo de cobertura, generando una falla controlada del pipeline.

![Coverage Fail](../docs/coverage-fail.png)

Resultado:
- el pipeline exige cobertura mínima  
- se asegura calidad estructural del código  

---

## 🧪 Quality Gate Simulado

Este enfoque replica el comportamiento de herramientas como:

- SonarQube  
- Azure DevOps Quality Gates  

Aunque no se utiliza una herramienta externa, el pipeline cumple el mismo propósito:

- validar calidad automáticamente  
- bloquear despliegue si no se cumplen estándares  
- reducir deuda técnica  

---

## 🧠 Valor DevOps

Este módulo permite:

- aplicar **Shift Left Testing**  
- automatizar controles de calidad  
- asegurar estándares antes de producción  
- mejorar confiabilidad del software  

---

## 📌 Conclusión

El Quality Gate implementado garantiza que:

- solo código validado avanza en el pipeline  
- se mantienen estándares de desarrollo  
- se reduce riesgo en despliegues  

Este enfoque es clave en entornos DevOps modernos, donde la calidad es parte integral del proceso de entrega continua.
