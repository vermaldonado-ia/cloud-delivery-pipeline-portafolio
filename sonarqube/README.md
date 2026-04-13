# 🔍 Code Quality - Quality Gate

![Code Quality](https://img.shields.io/badge/Quality-Gate%20Implemented-blue)  
![Linting](https://img.shields.io/badge/Linting-Flake8-blueviolet)  
![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen)

Este módulo implementa un **Quality Gate dentro del pipeline CI/CD**, utilizando herramientas como `flake8` y `pytest-cov` para validar la calidad del código antes del despliegue.

Se plantea como una **aproximación práctica** a lo que herramientas como SonarQube realizan en entornos reales.

---

## 🎯 Objetivo

- Validar la calidad del código antes del despliegue  
- Detectar errores críticos de forma temprana  
- Asegurar estándares mínimos de desarrollo  
- Bloquear el pipeline si no se cumplen criterios definidos  

---

## ⚙️ Rol dentro del pipeline

El Quality Gate se ubica entre CI y CD, actuando como un punto de control obligatorio antes del despliegue.

Flujo conceptual:

CI (Tests + Coverage)  
↓  
Code Quality (flake8)  
↓  
CD (Deploy)  

---

## 🔍 Validaciones implementadas

### ✔ Coverage de pruebas

Se utiliza `pytest-cov` para medir el nivel de cobertura del código.

Resultado actual:

- Coverage total: **100%**

---

### ✔ Validación de errores críticos

Comando utilizado:

flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics

Detecta:

- Errores de sintaxis  
- Variables no definidas  
- Fallos críticos de ejecución  

---

### ✔ Calidad y mantenibilidad

Comando utilizado:

flake8 src --count --max-complexity=10 --max-line-length=88 --statistics

Evalúa:

- Complejidad ciclomática  
- Estándares de formato  
- Legibilidad del código  

---

## 🚫 Comportamiento del Quality Gate

El comportamiento implementado es:

- Si los tests fallan → ❌ el pipeline se detiene  
- Si la cobertura se ejecuta → 📊 se valida alcance de pruebas  
- Si `flake8` detecta errores → ❌ el job de calidad falla  
- Si calidad falla → 🚫 el despliegue no se ejecuta  

Esto se implementa mediante dependencias entre jobs en GitHub Actions:

- `quality` depende de `test`  
- `deploy` depende de `quality`  

---

## 🧪 Prueba de validación

Se realizó una prueba controlada introduciendo un error en el código:

def prueba():
    print(variable_no_definida)

Resultado:

- ❌ Falla en etapa de calidad  
- ⛔ Bloqueo del pipeline  
- 🚫 Deploy no ejecutado  

---

## 🧠 Enfoque aplicado

Se implementa un enfoque práctico de **Quality Gate**, donde herramientas ligeras permiten simular el control de calidad previo al despliegue.

Esto permite comprender cómo funcionan estos mecanismos en pipelines reales sin necesidad de una integración completa con plataformas externas.

---

## 📌 Alcance actual

Actualmente el pipeline cuenta con:

- Ejecución en GitHub Actions  
- Coverage real de pruebas  
- Validación automática de calidad  
- Control de flujo entre etapas  
- Despliegue en GitHub Pages  

---

## 🔮 Evolución futura

- Integración con SonarQube o SonarCloud  
- Definición de umbral mínimo de coverage  
- Métricas avanzadas (deuda técnica, duplicación)  
- Quality Gates configurables  

---

## 🏁 Conclusión

Se implementa un **Quality Gate automatizado dentro del pipeline CI/CD**, permitiendo asegurar que el código cumpla condiciones mínimas de calidad antes de avanzar en el flujo de entrega.
