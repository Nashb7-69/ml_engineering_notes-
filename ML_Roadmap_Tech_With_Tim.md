# Machine Learning Roadmap - The Tech With Tim Method (70% Practical / 30% Theory)

> **Philosophy:** Code first, understand later. No proofs. No tutorial hell. Build end-to-end projects in every phase. If you watched it, you must build it.

## Phase 1: Python Fundamentals & Data Libraries [Estimated Time: 3-4 Weeks]

- [x] **1.1 Core Python Syntax & Logic (Build the foundation)**
  - [x] Install Python 3.10+, VS Code, and set up virtual environments (`venv` / `conda`)
  - [x] Variables, data types, type casting, f-strings, and `input()`/`print()`
  - [x] Conditionals (`if/elif/else`) and loops (`for`, `while`, `enumerate`, `zip`)
  - [x] Functions (`def`, `*args/**kwargs`, `lambda`, scope, return values)
  - [x] Error handling (`try/except/finally`) and file I/O (`open`, `with`, `csv`, `json`)
- [x] **1.2 Core Data Structures (Must be fluent)**
  - [x] Lists (slicing, list comprehensions, `append/pop/sort/map/filter`)
  - [x] Dictionaries (key-value pairs, `.get()`, `.items()`, dict comprehensions)
  - [x] Tuples vs Sets vs Lists (when and why to use each)
  - [x] Strings manipulation and common methods
- [x] **1.3 OOP Basics (No deep dive, just enough for ML)**
  - [x] Classes, objects, `__init__`, `self`, instance vs class attributes
  - [x] Methods, inheritance basics, and `super()`
  - [x] Create a simple `Dataset` class to understand OOP in practice
- [x] **1.4 NumPy - Numerical Python**
  - [x] `np.array`, `shape`, `reshape`, `dtype`, `zeros/ones/arange/linspace`
  - [x] Indexing, slicing, boolean masking, and fancy indexing
  - [x] Vectorized operations, broadcasting rules, and `axis` parameter
  - [x] Dot product, matrix multiplication (`@`, `np.dot`), transpose, `np.random`
- [ ] **1.5 Pandas - Data Manipulation**
  - [ ] `pd.Series` and `pd.DataFrame` creation and inspection (`.head()`, `.info()`, `.describe()`)
  - [x] Indexing: `loc` vs `iloc`, conditional filtering
  - [ ] Handling missing data: `isnull()`, `dropna()`, `fillna()`
  - [ ] `groupby()`, `merge/join/concat`, `pivot_table`, `apply()` and `value_counts()`
  - [ ] Reading/writing data: `read_csv()`, `read_excel()`, `to_csv()`
- [ ] **1.6 Matplotlib & Seaborn - Data Visualization**
  - [ ] Matplotlib: `plt.plot()`, `plt.scatter()`, `plt.bar()`, `plt.hist()`, `subplots()`, labels/legends
  - [ ] Seaborn: `sns.heatmap()`, `sns.pairplot()`, `sns.boxplot()`, `sns.countplot()`
  - [ ] **MINI-PROJECT (70% Rule):** Load a real CSV (Kaggle - Titanic or Iris) -> Clean with Pandas -> Visualize 3 insights with Matplotlib/Seaborn -> Push to GitHub
- [ ] **Phase 1 Exit Criteria:** Can write Python scripts without tutorials and manipulate any CSV using only Pandas/NumPy/Matplotlib

## Phase 2: Applied Mathematics (No Proofs - Intuition Only) [Estimated Time: 2-3 Weeks]

> **Tech With Tim Rule:** Understand *what* it does and *why* we use it, not how to prove it. Watch 3Blue1Brown/StatQuest, then code it.

- [ ] **2.1 Linear Algebra - Conceptual Intuition**
  - [ ] Vectors and Matrices (what they represent: data points and datasets)
  - [ ] Vector operations: dot product, magnitude/norm, and cosine similarity intuition
  - [ ] Matrix multiplication (why it powers neural networks)
  - [ ] Eigenvectors & Eigenvalues (intuition only - what PCA uses them for)
  - [ ] Hands-on: Implement vector ops with NumPy, no manual math proofs
- [ ] **2.2 Statistics & Probability - The ML Engine**
  - [ ] Mean, median, mode, variance, standard deviation, and distributions
  - [ ] Normal/Gaussian distribution, skewed distributions, and central limit theorem (concept)
  - [ ] Probability basics, conditional probability, and Bayes' Theorem (intuition for Naive Bayes)
  - [ ] Correlation vs causation, p-value intuition, and sampling/bias
  - [ ] Hands-on: Use `pandas.describe()` and `sns.histplot()` to analyze a dataset's distribution
- [ ] **2.3 Calculus & Optimization - How Models Learn**
  - [ ] What is a derivative? (slope/rate of change - intuition with graphs)
  - [ ] What is an integral? (area under curve - conceptual only)
  - [ ] Concept of Gradients (direction of steepest ascent/descent)
  - [ ] Gradient Descent intuition (learning rate, convergence, local vs global minima)
  - [ ] Cost/Loss functions: MSE, MAE, Cross-Entropy (what they measure visually)
  - [ ] Hands-on: Visualize a simple `y = x^2` loss curve and gradient descent steps with Matplotlib
- [ ] **MINI-PROJECT (70% Rule):** Take any dataset -> Calculate and visualize all Phase 2 concepts entirely with code (no pen-and-paper proofs)
- [ ] **Phase 2 Exit Criteria:** Can explain gradients, Bayes, and dot products to a beginner without using a single formula proof

## Phase 3: Core Classic ML (Scikit-Learn) [Estimated Time: 6-8 Weeks]

> **Tech With Tim Core:** This is 80% practical. Every algorithm = `fit()` -> `predict()` -> `evaluate()` -> build a small project. Use `sklearn` only.

- [ ] **3.1 ML Setup & Workflow**
  - [ ] Train/Test split (`train_test_split`), random_state, and data leakage concept
  - [ ] Feature scaling: `StandardScaler`, `MinMaxScaler`, `OneHotEncoder`
  - [ ] Pipeline (`sklearn.pipeline.Pipeline`) and `ColumnTransformer`
  - [ ] Overfitting vs Underfitting, bias-variance tradeoff (visual intuition)
- [ ] **3.2 Supervised Learning - Regression**
  - [ ] Linear Regression (`LinearRegression`) and intuition (line of best fit + cost function)
  - [ ] Polynomial Regression and regularization intuition
  - [ ] Ridge (L2) & Lasso (L1) Regression (`Ridge`, `Lasso`)
  - [ ] Metrics: MAE, MSE, RMSE, R² Score
  - [ ] Hands-on: Predict house prices (Boston / California Housing dataset)
- [ ] **3.3 Supervised Learning - Classification**
  - [ ] Logistic Regression (`LogisticRegression`) - why it is classification, not regression
  - [ ] K-Nearest Neighbors (KNN) (`KNeighborsClassifier`, choosing `k` with elbow method)
  - [ ] Decision Trees (`DecisionTreeClassifier`, Gini vs Entropy, visualizing the tree)
  - [ ] Random Forest (`RandomForestClassifier`, bagging intuition, feature importance)
  - [ ] Support Vector Machines (SVM) (`SVC`, kernel intuition: linear, RBF)
  - [ ] Naive Bayes (`GaussianNB` - connect back to Bayes Theorem from Phase 2)
- [ ] **3.4 Unsupervised Learning**
  - [ ] K-Means Clustering (`KMeans`, choosing k with elbow & silhouette score)
  - [ ] Hierarchical Clustering (conceptual only - `AgglomerativeClustering`)
  - [ ] Dimensionality Reduction: PCA (`PCA`, explained variance ratio visualization)
  - [ ] Hands-on: Cluster customers (Mall Customers dataset) + Visualize PCA on digits dataset
- [ ] **3.5 Model Evaluation & Tuning (Critical)**
  - [ ] Classification metrics: Accuracy, Precision, Recall, F1-Score, `confusion_matrix`, `classification_report`
  - [ ] ROC-AUC, `roc_curve`, and Precision-Recall curve
  - [ ] Cross-Validation (`cross_val_score`, `KFold`, `StratifiedKFold`)
  - [ ] Hyperparameter tuning: `GridSearchCV` and `RandomizedSearchCV`
  - [ ] Hands-on: Compare 4 classifiers on same dataset and present metrics in a table
- [ ] **END-TO-END PROJECT (Avoid Tutorial Hell):** Pick ONE Kaggle Tabular Dataset -> Full pipeline: EDA -> Cleaning -> Scaling -> Train 3+ models -> Tune -> Evaluate -> Write README and publish to GitHub
- [ ] **Phase 3 Exit Criteria:** Can build, evaluate, and compare any classic ML model from scratch using Scikit-Learn docs alone

## Phase 4: Deep Learning & Neural Networks (PyTorch) [Estimated Time: 8-10 Weeks]

> **Tech With Tim Rule:** Use PyTorch, not theory-heavy math. Understand tensors, autograd, and layer stacking. Build networks, don't prove backpropagation.

- [ ] **4.1 PyTorch Fundamentals**
  - [ ] Install PyTorch, check `torch.cuda.is_available()`, CPU vs GPU tensors
  - [ ] Tensors vs NumPy arrays: `torch.tensor`, `reshape`, `view`, `unsqueeze`, operations
  - [ ] Autograd (`requires_grad`, `.backward()`, `.grad`) - intuition only
  - [ ] `torch.nn.Module`, `Dataset` and `DataLoader` classes
  - [ ] Training loop: `forward()` -> `loss` -> `backward()` -> `optimizer.step()` -> `zero_grad()`
- [ ] **4.2 Artificial Neural Networks (ANN / Feed-Forward)**
  - [ ] Perceptron, activation functions: `ReLU`, `Sigmoid`, `Softmax`, `Tanh`
  - [ ] Loss functions: `nn.MSELoss`, `nn.CrossEntropyLoss`, `nn.BCELoss`
  - [ ] Optimizers: `SGD`, `Adam`, learning rate and epochs intuition
  - [ ] Build ANN: `nn.Sequential` or custom `nn.Module` (Input -> Hidden -> Output layers)
  - [ ] Hands-on: ANN on MNIST or Fashion-MNIST with `torchvision`
  - [ ] Track with `torch.utils.tensorboard` or loss curve via Matplotlib
- [ ] **4.3 Convolutional Neural Networks (CNNs)**
  - [ ] Convolution, filters/kernels, stride, padding, pooling (`MaxPool2d`) intuition (visual)
  - [ ] Layers: `nn.Conv2d`, `nn.MaxPool2d`, `nn.Flatten`, `nn.Linear`
  - [ ] Architecture intuition: LeNet, VGG, ResNet (concepts, don't code from paper)
  - [ ] Data augmentation: `torchvision.transforms` (Rotate, Flip, Normalize)
  - [ ] Transfer Learning: `torchvision.models.resnet18(pretrained=True)` + fine-tuning
  - [ ] Hands-on: CNN on CIFAR-10 or Cats vs Dogs - Compare ANN vs CNN accuracy
- [ ] **4.4 Recurrent Neural Networks (RNN / LSTM)**
  - [ ] Why sequences need memory: RNN vs ANN/CNN intuition
  - [ ] Vanilla RNN problems: Vanishing gradients intuition
  - [ ] LSTM & GRU intuition (gates: forget, input, output - conceptual)
  - [ ] Layers: `nn.RNN`, `nn.LSTM`, `nn.GRU`, handling hidden states
  - [ ] Text preprocessing: Tokenization, `torchtext` or `nltk`, embeddings (`nn.Embedding`)
  - [ ] Hands-on: Sentiment Analysis (IMDB Reviews) or Time-Series prediction with LSTM
- [ ] **4.5 Transformers - Basic Understanding**
  - [ ] Attention mechanism intuition (what it pays attention to - no math proof)
  - [ ] Self-attention, Multi-head attention, Encoder-Decoder concept
  - [ ] Use pre-trained transformers via `transformers` library (Hugging Face `pipeline`)
  - [ ] Hands-on: Run `pipeline('sentiment-analysis')` and fine-tune `bert-base-uncased` on a small text dataset
  - [ ] Understand tokens, positional encoding, and why Transformers replaced RNNs
- [ ] **END-TO-END PROJECT (70% Rule):** Choose ONE: Image Classifier (CNN + Transfer Learning) OR Text Classifier (LSTM/Transformer) -> Full PyTorch training loop -> Evaluate -> Save model with `torch.save()`
- [ ] **Phase 4 Exit Criteria:** Can code a training loop from memory and adapt a PyTorch tutorial to a new dataset without copying code blindly

## Phase 5: MLOps, Data Cleaning & Deployment [Estimated Time: 4-6 Weeks]

> **Tech With Tim Rule:** An undeployed model is an unfinished project. Learn to ship.

- [ ] **5.1 Data Cleaning & Feature Engineering (Real World Data)**
  - [ ] Handle missing values (strategies by column type), duplicates, outliers (IQR method)
  - [ ] Handling categorical data: One-Hot, Label Encoding, Target Encoding
  - [ ] Feature engineering: date features, text length, binning, log transforms
  - [ ] Imbalanced data: `SMOTE`, class weights, `stratify` parameter
  - [ ] Practice on a messy Kaggle dataset (Titanic, House Prices - the dirty version)
- [ ] **5.2 Git & GitHub (Learn in Public)**
  - [ ] `git init`, `add`, `commit`, `push`, `pull`, `.gitignore` for `venv` and `data/`
  - [ ] Branching (`git branch/checkout`) and meaningful commit messages
  - [ ] Create `README.md` with project description, metrics, and how to run
  - [ ] Push every Phase project to GitHub - commit at least 3x per week
- [ ] **5.3 API Deployment with FastAPI**
  - [ ] FastAPI basics: `FastAPI()`, `@app.get()`, `@app.post()`, `uvicorn` server
  - [ ] Pydantic models for request validation (`BaseModel`)
  - [ ] Load pickled model (`pickle`/`joblib` for sklearn, `torch.load` for PyTorch) and serve predictions
  - [ ] Test with Swagger UI (`/docs`) and `curl` / Postman
  - [ ] Hands-on: Wrap any Phase 3 model in a `/predict` endpoint
- [ ] **5.4 Docker - Containerization**
  - [ ] Dockerfile basics: `FROM`, `COPY`, `RUN pip install`, `CMD ["uvicorn"...]`
  - [ ] Build: `docker build -t ml-api .` and run: `docker run -p 8000:8000 ml-api`
  - [ ] `docker-compose.yml` (optional) and `.dockerignore`
- [ ] **5.5 Cloud Platforms Basics**
  - [ ] Choose one: Hugging Face Spaces / Render / Railway / AWS EC2 / Google Cloud Run
  - [ ] Deploy Dockerized FastAPI app to cloud (free tier)
  - [ ] Environment variables, requirements.txt, and basic logging
  - [ ] Alternative simple deploy: `Streamlit` or `Gradio` app for quick demos
- [ ] **CAPSTONE PROJECT (Build End-to-End):** Messy Dataset -> Full Cleaning & EDA -> Train Best Model (Sklearn or PyTorch) -> Wrap with FastAPI -> Dockerize -> Deploy to Cloud -> Link live URL in GitHub README -> Record 2-minute demo video
- [ ] **Phase 5 Exit Criteria:** Anyone on the internet can send data to your API and get a prediction from your model

## Golden Rules to Avoid Quitting [Estimated Time: Ongoing Mindset]

> **The Tech With Tim Philosophy - Read this when you feel stuck.**

- [ ] **Follow the 70/30 Rule - Always**
  - [ ] Spend 70% of time CODING/BUILDING and only 30% watching/reading theory
  - [ ] For every 1 hour of tutorial, spend 2+ hours modifying, breaking, and rebuilding it without guidance
  - [ ] If you understand 70% intuitively, move on - you will learn the rest by building
- [ ] **Avoid Tutorial Hell at All Costs**
  - [ ] NEVER finish a tutorial without changing the dataset, features, or model yourself
  - [ ] Delete the tutorial code and try to rewrite it from memory/docs within 24 hours
  - [ ] Limit to 1-2 quality tutorials per topic (Tech With Tim, StatQuest, docs) - then build solo
- [ ] **Build End-to-End, Not Just Notebooks**
  - [ ] Every major concept must end in a GitHub repo with: data + notebook/script + README + metrics
  - [ ] Prefer `.py` scripts and pipelines over endless Jupyter notebooks after Phase 3
  - [ ] A project is not done until it is deployed or shareable via API/demo
- [ ] **Learn in Public**
  - [ ] Push to GitHub at least 3 times per week, even if code is messy
  - [ ] Post progress on LinkedIn / X / Discord - explain one thing you learned this week
  - [ ] Document failures and lessons in your README - employers value process over perfection
- [ ] **Consistency > Intensity**
  - [ ] Code 60-90 minutes daily rather than 10 hours on weekends
  - [ ] If stuck for >45 minutes, ask in Discord/Stack Overflow, then move on and return later
  - [ ] Track streaks in Obsidian: use this checklist daily - checking boxes builds momentum
- [ ] **Done is Better Than Perfect**
  - [ ] Ship a 85% accurate model today rather than chasing 92% for a month
  - [ ] Iterate after deployment - real learning comes from improving shipped projects

---
[[MOC|← Vault Hub]] · [[python/README|Python Course]]
