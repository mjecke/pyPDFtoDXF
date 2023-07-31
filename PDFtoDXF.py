# !!!! Requires 'inkscape' and 'pdf2svg' to be in system path !!!!
# Tested with inkscape v1.2, pdf2svg v0.2.3_6, and PyPDF2 v3.0.1

import os
import subprocess
from PyPDF2 import PdfReader
import argparse

def extract_pages_as_svg(pdf_file, output_dir):
    with open(pdf_file, 'rb') as file:
        pdf = PdfReader(file)
        num_pages = len(pdf.pages)

    for i in range(num_pages):
        output_file = os.path.join(output_dir, f'{os.path.splitext(os.path.basename(pdf_file))[0]}_{i}.svg')
        subprocess.run(['pdf2svg', pdf_file, output_file, str(i+1)], check=True)

def convert_svg_to_dxf(svg_file, dxf_file):
    subprocess.run(['inkscape', svg_file, '--export-type=dxf', '-o', dxf_file], check=True)

def extract_and_convert(pdf_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    extract_pages_as_svg(pdf_file, output_dir)
    svg_files = [f for f in os.listdir(output_dir) if f.endswith('.svg')]
    
    for svg_file in svg_files:
        dxf_file = os.path.join(output_dir, f'{os.path.splitext(svg_file)[0]}.dxf')
        convert_svg_to_dxf(os.path.join(output_dir, svg_file), dxf_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract SVGs from PDF and convert to DXF.')
    parser.add_argument('pdf_file', type=str, help='Input PDF file')
    parser.add_argument('output_dir', type=str, help='Output directory')
    args = parser.parse_args()
    
    extract_and_convert(args.pdf_file, args.output_dir)

