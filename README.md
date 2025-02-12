# pptx2pdf

一个简单的工具，用于将目录下的所有PPT文件（.pptx）转换为PDF格式。

## 依赖要求
- Python 3.x
- LibreOffice
- python-pptx >= 0.6.21

## 安装
1. 确保已安装 LibreOffice
2. 安装 Python 依赖:

## 接口说明

```python
convert_ppt_to_pdf(input_dir)
```
**description:**
将目录下的所有PPT文件（.pptx）转换为PDF格式,转换后文件在input_dir/pdf目录下
**param:**
- input_dir: 输入的PPT文件目录
**return:**
None

## 使用示例

```bash
python pptx2pdf.py /path/to/pptx/directory
