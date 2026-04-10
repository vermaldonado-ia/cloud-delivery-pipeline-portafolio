# 🔍 Code Quality - Quality Gate

![Code Quality](https://img.shields.io/badge/Quality-Gate%20Implemented-blue)
![Linting](https://img.shields.io/badge/Linting-Flake8-blueviolet)
![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen)

Este módulo implementa un **Quality Gate dentro del pipeline CI/CD**, replicando el comportamiento de herramientas como **SonarQube**, mediante el uso de `flake8` y complementando la validación con cobertura real utilizando `pytest-cov`.

---

## 🎯 Objetivo

* Validar la calidad del código antes del despliegue
* Detectar errores críticos de forma temprana
* Asegurar estándares mínimos de desarrollo
* Bloquear el pipeline si no se cumplen criterios definidos

---

## ⚙️ Rol dentro del pipeline

```text
CI (Tests + Coverage)
 ↓
Code Quality (flake8)
 ↓
CD (Deploy)
```

El Quality Gate se ubica entre CI y CD, actuando como un punto de control obligatorio antes del despliegue.

---

## 🔍 Validaciones implementadas

### ✔ Coverage de pruebas (real)

Se utiliza `pytest-cov` para medir el nivel de cobertura del código.

**Resultado actual:**

* Coverage total: **100%**

---

### ✔ Validación de errores críticos

```bash
flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
```

Detecta:

* Errores de sintaxis
* Variables no definidas
* Fallos críticos de ejecución

---

### ✔ Calidad y mantenibilidad

```bash
flake8 src --count --max-complexity=10 --max-line-length=88 --statistics
```

Evalúa:

* Complejidad ciclomática
* Estándares de formato
* Legibilidad del código

---

## 🚫 Comportamiento del Quality Gate

El comportamiento implementado es:

* Si los tests fallan → ❌ pipeline se detiene
* Si la cobertura se ejecuta correctamente → 📊 se valida alcance de pruebas
* Si `flake8` detecta errores → ❌ job de calidad falla
* Si calidad falla → 🚫 el despliegue no se ejecuta

Esto se implementa mediante dependencias entre jobs en GitHub Actions:

```yaml
quality:
  needs: test

deploy:
  needs: quality
```

---

## 🧪 Prueba de validación

Se realizó una prueba controlada introduciendo un error en el código:

```python
def prueba():
    print(variable_no_definida)
```

### Resultado

* ❌ Falla en etapa de calidad
* ⛔ Bloqueo del pipeline
* 🚫 Deploy no ejecutado

---

## 🧠 Enfoque aplicado

Este enfoque implementa un **Quality Gate funcional**, donde herramientas ligeras como `flake8` cumplen el rol equivalente al control de calidad que normalmente se gestiona mediante plataformas como SonarQube.

---

## 📌 Alcance actual

Actualmente el pipeline cuenta con:

* Ejecución real en GitHub Actions
* Coverage real de pruebas
* Validación automática de calidad
* Control de flujo entre etapas
* Despliegue real en GitHub Pages

---

## 🔮 Evolución futura

* Integración con SonarQube o SonarCloud
* Definición de umbral mínimo de coverage
* Métricas avanzadas (deuda técnica, duplicación)
* Quality Gates configurables por entorno

---

## 🏁 Conclusión

Se implementa un **Quality Gate automatizado dentro del pipeline CI/CD**, asegurando que solo código que cumple estándares de calidad y cobertura pueda avanzar a despliegue, replicando prácticas utilizadas en entornos DevOps profesionales.

---
