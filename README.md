# matlib

`matlib` 是一个面向教学和原型验证的矩阵/向量小库，适合快速做线代运算实验。

## 功能概览

- `Matrix`：矩阵加减、矩阵乘法、转置、2x2 与 3x3 行列式
- `Vector`：点积、3D 叉积、向量归一化
- `identity(n)`：创建 n 阶单位矩阵
- `zeros(m, n)`：创建 m×n 零矩阵

## 快速使用

```bash
pip install -e .
```

```python
from matlib import Matrix, Vector, identity, zeros

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])
print((a + b).data)
print(a.transpose().data)
print(identity(3).data)
print(zeros(2, 3).data)

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1.dot(v2))
print(v1.cross(v2).values)
```

## 测试

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytest tests/ -v --tb=short --json-report --json-report-file=test_results.json
```
