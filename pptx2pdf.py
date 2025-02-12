import os
from pathlib import Path
from pptx import Presentation
import subprocess
import argparse

def convert_ppt_to_pdf(input_dir):
    # 创建 pdf 子文件夹
    pdf_dir = Path(input_dir) / 'pdf'
    pdf_dir.mkdir(exist_ok=True)
    
    # 遍历目录下的所有文件
    for file in Path(input_dir).glob('*.[pP][pP][tT][xX]'):
        try:
            output_pdf = pdf_dir / file.with_suffix('.pdf').name
            # 使用 LibreOffice 进行转换
            subprocess.run([
                'soffice',
                '--headless',
                '--convert-to', 'pdf',
                str(file.absolute()),
                '--outdir', str(pdf_dir)
            ])
            print(f'成功转换: {file.name} -> {output_pdf.name}')
        except Exception as e:
            print(f'转换失败 {file.name}: {str(e)}')

if __name__ == '__main__':
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='将PPT文件转换为PDF')
    parser.add_argument('directory', help='要处理的目录路径')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    if os.path.exists(args.directory):
        convert_ppt_to_pdf(args.directory)
    else:
        print('指定的目录不存在!')
