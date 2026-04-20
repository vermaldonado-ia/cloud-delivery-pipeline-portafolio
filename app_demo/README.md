# 🧪 App Demo – Validación CI y Quality Gate

Este módulo corresponde a una aplicación de ejemplo desarrollada en Python, utilizada exclusivamente para demostrar prácticas de **Integración Continua (CI)** y control de calidad dentro del pipeline DevOps.

⚠️ **Importante:**
Esta aplicación **no es desplegada en producción**. Su propósito es validar automáticamente la calidad del código antes de permitir cambios en la rama principal.

---

## 🎯 Objetivo

Demostrar cómo un pipeline de CI permite:

* Detectar errores de forma temprana (Shift Left)
* Validar la correcta instalación de dependencias
* Ejecutar pruebas automatizadas
* Medir cobertura de código
* Aplicar un criterio de calidad (Quality Gate) antes del merge

---

## ⚙️ Rol dentro del Pipeline

Este módulo representa la **etapa de validación técnica** dentro del flujo DevOps:

Pull Request / Push
↓
CI (Tests + Coverage)
↓
Quality Gate
↓
Merge controlado a main
↓
CD (Deploy de sitio estático en AWS Amplify)

📌 La etapa de CD despliega un **sitio estático (`index.html`)**, el cual actúa como evidencia del pipeline, pero **no corresponde a esta aplicación Python**.

---

## 🧩 Estructura del Proyecto

```
app_demo/
│
├── main.py
├── requirements.txt
├── tests/
│   └── test_main.py
└── README.md
```

---

## 🔄 Proceso de CI Implementado

El pipeline ejecuta automáticamente las siguientes acciones:

### 1. Configuración del entorno

* Instalación de Python
* Instalación de dependencias desde `requirements.txt`

### 2. Ejecución de pruebas

* Uso de `pytest` para validar funcionalidad

### 3. Medición de cobertura

* Uso de `pytest-cov`
* Generación de reporte de coverage

### 4. Quality Gate

* Se exige un mínimo de **80% de cobertura**
* Si no se cumple, el pipeline falla

---

## 🧪 Ejecución local

Para ejecutar la aplicación y pruebas en entorno local:

```bash
cd app_demo
python -m venv venv
source venv/bin/activate  # En Mac/Linux
pip install -r requirements.txt
pytest --cov=src
```

---

## 🛠️ Herramientas utilizadas

* Python 3.11
* pytest
* pytest-cov
* GitHub Actions

---

## 💡 Enfoque del Diseño

Este módulo fue diseñado bajo el principio:

👉 *"Primero asegurar calidad, luego permitir despliegue"*

Por esta razón:

* La validación CI está desacoplada del CD
* El pipeline garantiza estándares mínimos antes de integrar cambios
* Se simula un entorno real donde la calidad es una puerta de entrada obligatoria

---

## 🚀 Valor en un contexto real

En un entorno empresarial, este enfoque permite:

* Reducir defectos en producción
* Asegurar estándares de desarrollo
* Controlar el flujo de cambios hacia ramas principales
* Implementar prácticas DevOps alineadas con calidad desde el inicio

---

## 📌 Nota final

Este módulo forma parte del repositorio:

👉 **Cloud Delivery Pipeline Portafolio**

Donde se demuestra un flujo completo que integra:

* CI con validación de calidad (este módulo)
* CD con despliegue en AWS Amplify (sitio estático)

Ambos componentes juntos representan un pipeline DevOps funcional a nivel demostrativo.
