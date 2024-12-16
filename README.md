# Repositorio de Implementaciones de OpenAI Gymnasium

Este repositorio contiene implementaciones de modelos de aprendizaje por refuerzo utilizando entornos de **OpenAI Gymnasium**. Los principales proyectos incluidos son:

## Contenido del Repositorio

- **PLE03.ipynb**: Notebook que implementa el agente **Bipedal Walker** utilizando el entorno `BipedalWalker-v3`. Se exploran técnicas como **Actor-Critic** y **Proximal Policy Optimization (PPO)** para entrenar al modelo a caminar en terrenos irregulares.

- **N02_PLE03_car.ipynb**: Notebook que desarrolla el agente para el problema de **Mountain Car** usando el entorno `MountainCar-v0`. Se implementa un algoritmo de **Q-Learning** para resolver el desafío del coche en la montaña.

- **requirements.txt**: Archivo de texto que lista las dependencias y paquetes necesarios para ejecutar los notebooks y scripts del repositorio.

- **validation.py**: Script de validación para comprobar la correcta instalación y funcionamiento del entorno `LunarLander-v3`.

- **validation_walker.py**: Script específico para validar el entorno `BipedalWalker-v3`.

- **Carpeta [`pesos`](pesos)**: Contiene los modelos entrenados y sus pesos correspondientes:

  - **pesos/mi_bipedal_walker.weights.h5**: Pesos del modelo entrenado para el Bipedal Walker.
  - **pesos/mountain_car.pkl**: Pesos del modelo entrenado para el Mountain Car.

- **Carpeta [`images`](images)**: carpeta donde se encuentran las ilustraciones usadas en los Notebooks.

- **.gitignore**: Archivo que especifica qué archivos o carpetas deben ser ignorados por Git. En este caso la `carpeta images`, donde están las ilustraciones de los Notebooks, estaba antes metida en este archivo. Sin embargo, para su buena renderización en web, se ha quitado del gitignore, aunque las imágenes en web no se están renderizando correctamente.

## Instalación y Ejecución

Siga los pasos a continuación para clonar el repositorio, instalar las dependencias y ejecutar los notebooks:

### 1. Clonar el Repositorio

Abra una terminal y ejecute:

```bash
git clone https://github.com/usuario/nombre_del_repositorio.git
```

### 2. Crear un Entorno Virtual (Opcional pero Recomendado)

Es recomendable usar un entorno virtual para evitar conflictos de dependencias:

- Con venv:

```bash
    python -m venv venv
```

- Con conda, se recomienda usar la versión de Python 3.11:

```bash
    conda create --name "nombre_entorno" python=3.11
```

## 3. Activación del Entorno Virtual

- En windows:

```bash
    venv\Scripts\activate
```

- En macOS/Linux:

```bash
    source venv/bin/activate
```

## 4. Instalar dependencias

Dentro del entorno virtual, instale las dependencias con:

```bash
pip install -r requirements.txt
```

## 5. Ejecutar Notebooks

Para ejecutar los Notebooks, utilice Jupyter Notebook o JupyterLab

```bash
jupyter notebook
```

Luego, en su navegador web, abra los archivos `PLE03.ipynb` o `N02_PLE03_car.ipynb` y ejecute las celdas según corresponda.

Si así lo prefiere, instale la extensión de Visual Studio Code de Jupyter Notebook junto a las bibliotecas requeridas para poder ejecutarlo en el entorno de desarrollo.

## 6. Notas adicionales

- Los _scripts de validación_ `(validation.py y validation_walker.py)` pueden ser utilizados para verificar que los entornos están configurados correctamente antes de ejecutar los modelos principales.

- Los _modelos pre-entrenados_ en la carpeta `pesos` pueden ser cargados para evitar tiempos de entrenamiento prolongados.
