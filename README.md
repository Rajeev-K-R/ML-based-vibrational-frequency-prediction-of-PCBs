# 📐 Machine Learning-Based Vibrational Frequency Prediction of PCBs

A machine learning approach for predicting the **resonant vibrational frequency / natural frequency of multilayer rectangular Printed Circuit Boards (PCBs)** from key geometric and construction parameters.

The project explores the use of machine learning as a computationally efficient alternative to repeatedly running conventional engineering simulations for frequency prediction.

## 🎯 Motivation

Printed Circuit Boards can experience mechanical vibration during operation, transportation, and testing. Their natural frequencies depend on several design and construction parameters, making vibration analysis an important part of PCB mechanical design.

Conventional simulation-based approaches can provide accurate results, but repeatedly performing simulations during the design process can be computationally expensive.

The idea behind this project is to develop a **machine-learning surrogate model**:

```text
PCB Design Parameters
        │
        ▼
   ML Model
        │
        ▼
Predicted Vibrational Frequency
```

Once trained, the model can provide a frequency estimate much faster than running a full numerical simulation for every new design.

## 🧠 How It Works

The project follows a supervised-learning workflow in which PCB parameters are used as input features and the corresponding vibrational frequency is used as the prediction target.

The main workflow is:

```text
Engineering / Simulation Data
            │
            ▼
     Data Preparation
            │
            ▼
     Feature Selection
            │
            ▼
  Multiple ML Regression Models
            │
            ▼
       Model Comparison
            │
            ▼
    Best Model Selection
            │
            ▼
  Vibrational Frequency Prediction
```

The current project focuses on predicting PCB vibrational behaviour from parameters including:

- **PCB length**
- **PCB width**
- **Copper percentage**

The project benchmarks multiple machine-learning approaches rather than relying on a single model. According to the project description, **12 ML models**, including neural-network and pretrained-model approaches, were evaluated, with **ExtraTreesRegressor** selected as the most suitable model for the current stage of the work.

## 🔬 Machine Learning Approach

A number of regression models are evaluated and compared using the available PCB dataset.

The general idea is:

```text
X = PCB design parameters
y = Vibrational frequency

X  ───────────────► Regression Model ───────────────► ŷ
                                                   │
                                                   ▼
                                         Predicted Frequency
```

Model performance is then compared to identify an appropriate surrogate model for the engineering problem.

### Why Extra Trees?

The current study identifies **ExtraTreesRegressor** as the most suitable model among the evaluated approaches.

Extra Trees is an ensemble of highly randomised decision trees. Each tree learns nonlinear relationships between the input PCB parameters and the target frequency, while the ensemble combines their predictions to improve robustness.

This is particularly useful for engineering problems where the relationship between geometric parameters and vibrational behaviour may not be well represented by a simple linear equation.

## ⚙️ Project Workflow

### 1. Prepare the Dataset

The project uses PCB design/simulation data containing the relevant design parameters and corresponding vibrational-frequency values.

### 2. Define Input Features

Important PCB parameters are extracted as model inputs, including:

```text
Length
Width
Copper Percentage
```

### 3. Train Multiple Models

Several regression models are trained on the same problem so that their predictive performance can be compared objectively.

### 4. Evaluate the Models

The models are evaluated using regression-performance metrics and their predictions are compared against the reference frequency values.

### 5. Select the Best Model

The best-performing approach is retained as the surrogate model for predicting PCB vibrational frequency.

### 6. Use the Model for Fast Prediction

Once trained, the model can be used to estimate the vibrational frequency of a new PCB configuration without running the full simulation workflow again.

## 📊 Why This Matters

The project explores an important engineering-computational idea:

> **Can an ML model learn the relationship between PCB design parameters and vibrational behaviour well enough to act as a fast surrogate for simulation?**

A successful surrogate model could reduce the cost of repeatedly evaluating candidate PCB designs and make design-space exploration faster.

This is especially relevant to engineering optimisation, where hundreds or thousands of candidate configurations may need to be evaluated.

## 🛠️ Technologies

- **Python**
- **NumPy**
- **Pandas**
- **Scikit-learn**
- Machine Learning Regression
- Engineering / Vibrational Analysis

## 📁 Repository Structure

```text
ML-based-vibrational-frequency-prediction-of-PCBs/
│
├── ML model for simulation/
│   └── ML implementation
│
├── .gitignore
└── .gitattributes
```

The repository currently organises the main implementation under the `ML model for simulation` directory.

## 🚀 Future Work

The current project establishes an ML-based surrogate modelling approach for PCB vibrational-frequency prediction.

Planned directions include investigating:

- **Gaussian Process Regression**
- Other **Bayesian regression methods**
- Improved uncertainty estimation
- Larger and more diverse simulation datasets
- More PCB design parameters
- Integration with engineering design optimisation workflows

The longer-term objective is to move from simply predicting vibrational frequency toward using machine learning as part of a faster **simulation-replacement / design-optimisation pipeline**.

## 🎓 Project Context

This project sits at the intersection of **mechanical engineering, vibration analysis, numerical simulation, and machine learning**.

It explores how computationally expensive engineering relationships can be approximated using data-driven surrogate models, with the eventual goal of accelerating engineering analysis and design iteration.

## 📄 License

See the repository for licensing information.
