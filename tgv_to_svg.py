import re
import os
from pathlib import Path

def extract_svg_from_tgv(tgv_content):
    """从TGV内容中提取SVG标签部分"""
    # 使用正则表达式匹配<svg>...</svg>标签及其内容
    svg_match = re.search(r'<svg.*?</svg>', tgv_content, re.DOTALL)
    if svg_match:
        return svg_match.group(0)
    return None

def convert_tgv_to_svg(tgv_path, output_path=None):
    """将单个TGV文件转换为SVG文件"""
    # 读取TGV文件内容
    try:
        with open(tgv_path, 'r', encoding='utf-8') as f:
            tgv_content = f.read()
    except Exception as e:
        print(f"错误: 无法读取文件 {tgv_path}: {e}")
        return False
    
    # 提取SVG内容
    svg_content = extract_svg_from_tgv(tgv_content)
    if not svg_content:
        print(f"警告: {tgv_path} 中未找到有效的SVG标签内容")
        return False
    
    # 设置输出路径
    if not output_path:
        output_path = Path(tgv_path).with_suffix('.svg')
    
    # 写入SVG文件
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"转换成功: {tgv_path} -> {output_path}")
        return True
    except Exception as e:
        print(f"错误: 无法写入文件 {output_path}: {e}")
        return False

def batch_convert_tgv_to_svg():
    """批量转换当前目录下所有.tgv文件为.svg文件"""
    current_dir = Path.cwd()
    tgv_files = list(current_dir.glob('*.tgv'))
    
    if not tgv_files:
        print("当前目录下未找到任何.tgv文件")
        return
    
    print(f"找到 {len(tgv_files)} 个.tgv文件，开始转换...")
    print("=" * 50)
    
    success_count = 0
    for tgv_file in tgv_files:
        if convert_tgv_to_svg(tgv_file):
            success_count += 1
    
    print("=" * 50)
    print(f"转换完成: 成功 {success_count}/{len(tgv_files)} 个文件")

if __name__ == "__main__":
    batch_convert_tgv_to_svg()
    input("按Enter键退出...")  # 防止Windows下命令行窗口立即关闭