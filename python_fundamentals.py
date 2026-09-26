# Python Fundamentals - Complete Practice File
# Tech With Tim Style: 70% Practice - Run it, break it, modify it!

# ============================================================
# 1. SYNTAX, VARIABLES & DATA TYPES
# ============================================================
print("=== 1. Variables & Types ===")
name = "Ravox"
age = 22
height = 5.9
is_learning = True

print(f"Name: {name}, Age: {age}, Height: {height}")
print(type(name), type(age), type(height), type(is_learning))

# Type casting
x = "100"
print(int(x) + 50)  # 150
print(float("3.14"))

# Input (uncomment to try)
# user_input = input("Enter your name: ")
# print(f"Hello {user_input}")

# ============================================================
# 2. CONDITIONALS & LOOPS
# ============================================================
print("\n=== 2. Conditionals ===")
score = 85
if score >= 90:
    print("A grade")
elif score >= 75:
    print("B grade")
else:
    print("C grade")

# Ternary operator
status = "pass" if score > 50 else "fail"
print(status)

print("\n=== Loops ===")
for i in range(5):
    print(f"Count: {i}")

for i, char in enumerate("Python"):
    print(f"Index {i}: {char}")

# Zip
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 88]
for n, s in zip(names, scores):
    print(f"{n} scored {s}")

# While loop
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

# List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {squares}")

# ============================================================
# 3. FUNCTIONS
# ============================================================
print("\n=== 3. Functions ===")

def greet(name, lang="en"):
    return f"Hello {name}!" if lang == "en" else f"Bonjour {name}!"

print(greet("Ravox"))
print(greet("Ravox", "fr"))

def add(*args):
    return sum(args)

print(add(1, 2, 3, 4, 5))  # 15

def info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

info(name="Ravox", field="ML", level="beginner")

# Lambda
multiply = lambda x, y: x * y
print(multiply(6, 7))  # 42

# Map & Filter
nums = [1, 2, 3, 4, 5, 6]
doubled = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Doubled: {doubled}")
print(f"Evens: {evens}")

# ============================================================
# 4. DATA STRUCTURES - LISTS
# ============================================================
print("\n=== 4. Lists ===")
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
fruits.insert(1, "grape")
print(fruits)
print(fruits[1:3])  # slicing
print(fruits[-1])   # last element

fruits.sort()
print(f"Sorted: {fruits}")
fruits.reverse()
print(f"Reversed: {fruits}")

# List methods
nums = [3, 1, 4, 1, 5, 9, 2]
print(f"Length: {len(nums)}, Min: {min(nums)}, Max: {max(nums)}, Sum: {sum(nums)}")
print(f"Count of 1: {nums.count(1)}")
print(f"Index of 5: {nums.index(5)}")

# ============================================================
# 5. DICTIONARIES, TUPLES, SETS
# ============================================================
print("\n=== 5. Dicts, Tuples, Sets ===")

# Dictionary
student = {
    "name": "Ravox",
    "age": 22,
    "skills": ["Python", "ML"],
    "active": True
}
print(student["name"])
print(student.get("grade", "Not found"))  # safe get
student["city"] = "Paris"
for k, v in student.items():
    print(f"{k} -> {v}")

# Dict comprehension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)

# Tuple (immutable)
coords = (10, 20)
x, y = coords  # unpacking
print(f"x={x}, y={y}")

# Set (unique values)
a = {1, 2, 3, 3, 4}
b = {3, 4, 5, 6}
print(f"Set a: {a}")  # {1,2,3,4}
print(f"Intersection: {a & b}")
print(f"Union: {a | b}")
print(f"Difference: {a - b}")

# Strings
text = "  Hello Python World  "
print(text.strip())
print(text.lower())
print(text.replace("Python", "ML"))
print(text.split())
print("-".join(["ML", "is", "fun"]))

# ============================================================
# 6. ERROR HANDLING & FILE I/O
# ============================================================
print("\n=== 6. Error Handling ===")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Always runs")

try:
    num = int("abc")
except ValueError:
    print("Invalid number!")

# File I/O
with open("demo.txt", "w") as f:
    f.write("Hello ML World\n")
    f.write("Python is awesome\n")

with open("demo.txt", "r") as f:
    content = f.read()
    print(content)

# Working with JSON & CSV
import json
data = {"name": "Ravox", "scores": [90, 85, 88]}
with open("demo.json", "w") as f:
    json.dump(data, f, indent=2)

with open("demo.json", "r") as f:
    loaded = json.load(f)
    print(loaded)

import csv
with open("demo.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["Alice", 90])
    writer.writerow(["Bob", 85])

with open("demo.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# ============================================================
# 7. OOP BASICS
# ============================================================
print("\n=== 7. OOP ===")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def __str__(self):
        return f"Student({self.name}, avg={self.average():.1f})"

s1 = Student("Ravox", 22)
s1.add_score(90)
s1.add_score(85)
print(s1)
print(f"Average: {s1.average()}")

# Inheritance
class GradStudent(Student):
    def __init__(self, name, age, thesis):
        super().__init__(name, age)
        self.thesis = thesis

    def __str__(self):
        return f"GradStudent({self.name}, thesis={self.thesis})"

g1 = GradStudent("Alice", 24, "Deep Learning")
g1.add_score(95)
print(g1)

# Simple Dataset class (ML style)
class Dataset:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

ds = Dataset([10, 20, 30, 40])
print(f"Dataset length: {len(ds)}, item 2: {ds[2]}")

# ============================================================
# 8. NUMPY
# ============================================================
print("\n=== 8. NumPy ===")
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}, shape: {arr.shape}, dtype: {arr.dtype}")

zeros = np.zeros((2, 3))
ones = np.ones((2, 2))
print(f"Zeros:\n{zeros}")
print(f"Ones:\n{ones}")

rng = np.arange(0, 10, 2)  # 0,2,4,6,8
lin = np.linspace(0, 1, 5)  # 5 points between 0 and 1
print(f"Arange: {rng}")
print(f"Linspace: {lin}")

mat = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Matrix:\n{mat}")
print(f"Transpose:\n{mat.T}")
print(f"Reshaped to 3x2:\n{mat.reshape(3, 2)}")

# Indexing & Slicing
print(f"First row: {mat[0]}")
print(f"Element [1,2]: {mat[1, 2]}")
print(f"Boolean mask >3: {mat[mat > 3]}")

# Vectorized ops & Broadcasting
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"a + b = {a + b}")
print(f"a * 2 = {a * 2}")
print(f"Dot: {np.dot(a, b)}")  # 32
print(f"Matmul: {a @ b}")

# Axis
data = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Sum all: {np.sum(data)}")
print(f"Sum axis 0 (cols): {np.sum(data, axis=0)}")
print(f"Sum axis 1 (rows): {np.sum(data, axis=1)}")
print(f"Mean: {np.mean(data)}")

# Random
np.random.seed(42)
rand_arr = np.random.randn(2, 3)
print(f"Random:\n{rand_arr}")
rand_int = np.random.randint(0, 100, size=5)
print(f"Random ints: {rand_int}")

# ============================================================
# 9. PANDAS
# ============================================================
print("\n=== 9. Pandas ===")
import pandas as pd

# From dict
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 22, 35],
    "score": [90, 85, None, 88],
    "city": ["Paris", "London", "Paris", "Berlin"]
})
print(df)
print(df.head(2))
print(df.info())
print(df.describe())
print(df["age"].value_counts())

# Indexing
print(df.loc[0])  # by label
print(df.iloc[0])  # by position
print(df[df["age"] > 25])  # filtering

# Missing data
print(f"Nulls:\n{df.isnull().sum()}")
df_filled = df.fillna(df["score"].mean())
print(f"Filled:\n{df_filled}")

# Groupby
print(df.groupby("city")["score"].mean())

# Apply
df["age_group"] = df["age"].apply(lambda x: "Young" if x < 30 else "Senior")
print(df)

# Merge
df2 = pd.DataFrame({"name": ["Alice", "Bob"], "salary": [50000, 60000]})
merged = pd.merge(df, df2, on="name", how="left")
print(f"Merged:\n{merged}")

# Read/Write (creates files)
df.to_csv("students.csv", index=False)
print("Saved to students.csv")
print(pd.read_csv("students.csv").head())

# ============================================================
# 10. MATPLOTLIB & SEABORN — Polished (looks good on graph & in markdown)
# ============================================================
print("\n=== 10. Visualization (Polished) ===")
import matplotlib.pyplot as plt
import seaborn as sns
import shutil
from pathlib import Path

# --- polished style ---
plt.rcParams.update({
    "figure.dpi": 200, "savefig.dpi": 200,
    "font.family": "sans-serif",
    "font.sans-serif": ["Inter", "Helvetica", "Arial", "DejaVu Sans"],
    "axes.titlesize": 11, "axes.labelsize": 9,
    "xtick.labelsize": 8, "ytick.labelsize": 8,
    "legend.fontsize": 8,
})
sns.set_theme(style="whitegrid", palette="deep", rc={"axes.grid": True, "grid.alpha": 0.25})

# 1) Trio: line + scatter + histogram
x = np.linspace(0, 10, 200)
y = np.sin(x)
fig, axes = plt.subplots(1, 3, figsize=(12, 3.8), constrained_layout=True)
fig.suptitle("Python Fundamentals — Polished Visual Trio", fontsize=13, weight="bold", y=1.02)

ax = axes[0]
ax.plot(x, y, color="#277da1", linewidth=2.2, label="sin(x)")
ax.fill_between(x, y, alpha=0.15, color="#277da1")
ax.scatter([np.pi/2, 3*np.pi/2], [1, -1], color="#f94144", s=40, zorder=5, edgecolor="white", linewidth=0.8)
ax.annotate("max", xy=(np.pi/2, 1), xytext=(np.pi/2+0.6, 0.7), fontsize=7, color="#333", arrowprops=dict(arrowstyle="->", color="#f94144", lw=1))
ax.annotate("min", xy=(3*np.pi/2, -1), xytext=(3*np.pi/2+0.6, -0.7), fontsize=7, color="#333", arrowprops=dict(arrowstyle="->", color="#f94144", lw=1))
ax.set_title("Line — sin(x)", weight="semibold")
ax.set_xlabel("x"); ax.set_ylabel("sin(x)"); ax.set_xlim(0, 10); ax.set_ylim(-1.15, 1.15)
ax.legend(frameon=True, facecolor="white", edgecolor="#ddd")

ax = axes[1]
plot_df = df.dropna(subset=["score"])
palette = {"Paris": "#43aa8b", "London": "#f3722c", "Berlin": "#577590"}
sns.scatterplot(data=plot_df, x="age", y="score", hue="city", s=90, alpha=0.85, edgecolor="white", linewidth=0.9, palette=palette, ax=ax)
for _, row in plot_df.iterrows():
    ax.text(row["age"]+0.3, row["score"]+0.15, row["name"], fontsize=7, color="#222", weight="500")
ax.set_title("Scatter — Age vs Score (by City)", weight="semibold")
ax.set_xlabel("Age"); ax.set_ylabel("Score"); ax.set_ylim(84, 91.5)
ax.legend(title="City", frameon=True, facecolor="white", edgecolor="#ddd", loc="lower right")

ax = axes[2]
ages = np.array([25, 30, 22, 35, 26, 28, 24, 33, 29, 27, 31])
sns.histplot(ages, bins=6, color="#90be6d", edgecolor="white", linewidth=1.1, alpha=0.85, ax=ax, kde=True)
sns.rugplot(df["age"], color="#f94144", height=0.08, ax=ax, linewidth=1.8)
ax.set_title("Histogram — Age Distribution (+ KDE)", weight="semibold")
ax.set_xlabel("Age"); ax.set_ylabel("Count"); ax.set_xlim(20, 36)

for a in axes:
    a.set_facecolor("white")
fig.patch.set_facecolor("white")
plt.savefig("demo_plot.png", bbox_inches="tight", facecolor="white")
Path("assets").mkdir(exist_ok=True)
shutil.copy("demo_plot.png", "assets/demo_plot.png")
print("Saved demo_plot.png (polished)")

# 2) Boxplot
plt.figure(figsize=(6.2, 4.2), constrained_layout=True)
ax = plt.gca()
sns.boxplot(data=df, x="city", y="score", hue="city", palette=palette, dodge=False, width=0.55, linewidth=1.1, fliersize=4, ax=ax, legend=False)
sns.stripplot(data=df, x="city", y="score", color="#222", size=7, alpha=0.7, edgecolor="white", linewidth=0.7, jitter=0.12, ax=ax)
ax.set_title("Boxplot — Score by City (with strip)", weight="bold", fontsize=12, pad=12)
ax.set_xlabel("City"); ax.set_ylabel("Score"); ax.set_ylim(83, 92)
for city in df["city"].unique():
    mean_val = df[df["city"]==city]["score"].mean()
    if np.isnan(mean_val):
        continue
    xpos = list(df["city"].unique()).index(city)
    ax.text(xpos, mean_val+0.35, f"mean {mean_val:.1f}", ha="center", fontsize=7, color="#333", weight="600",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#ddd", alpha=0.9))
ax.set_facecolor("white"); plt.gcf().patch.set_facecolor("white")
plt.savefig("seaborn_demo.png", bbox_inches="tight", facecolor="white")
shutil.copy("seaborn_demo.png", "assets/seaborn_demo.png")
print("Saved seaborn_demo.png (polished)")

# 3) Heatmap
plt.figure(figsize=(5.2, 4.4), constrained_layout=True)
df_num = df.copy()
df_num["salary"] = [50000, 60000, 55000, 62000]
import numpy as _np
_np.random.seed(0)
df_num["exp"] = df_num["age"] - 22 + _np.random.randn(4)*0.5
df_num["score_filled"] = df_num["score"].fillna(df_num["score"].mean())
corr = df_num.select_dtypes(include=[_np.number]).corr()
mask = _np.triu(_np.ones_like(corr, dtype=bool), k=1)
cmap = sns.diverging_palette(220, 20, as_cmap=True)
ax = sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap=cmap, vmin=-1, vmax=1, center=0,
                 square=True, linewidths=1.5, linecolor="white", cbar_kws={"shrink": 0.8, "label": "correlation"},
                 annot_kws={"size": 8, "weight": "600"})
ax.set_title("Correlation Heatmap — Numeric Features", weight="bold", fontsize=12, pad=14)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha="right", fontsize=8)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=8)
plt.gcf().patch.set_facecolor("white")
plt.savefig("heatmap_demo.png", bbox_inches="tight", facecolor="white")
shutil.copy("heatmap_demo.png", "assets/heatmap_demo.png")
print("Saved heatmap_demo.png (polished)")
# plt.show() # uncomment to display

print("\n=== DONE! Now modify this file and build your own project ===")
print("Challenge: Load a Kaggle CSV with pandas -> Clean it -> Visualize 3 insights -> Push to GitHub")
