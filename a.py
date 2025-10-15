import os
import re

def convert_table_to_headings(part_range, prefix='netem_full_list_part'):
    for part_num in range(1, part_range + 1):
        filename = f"{prefix}{part_num}.md"
        if not os.path.exists(filename):
            print(f"文件不存在: {filename}")
            continue

        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        out_lines = []
        for line in lines:
            # 跳过表头和分隔线
            if line.strip().startswith('|') and not line.strip().startswith('| ---'):
                # 拆分表格行
                cols = [c.strip() for c in line.strip().strip('|').split('|')]
                if len(cols) >= 4 and cols[0].isdigit():
                    index = cols[0]
                    word = cols[2]
                    meaning = cols[3]
                    others = cols[4] if len(cols) > 4 else ''
                    out_lines.append(f"### {index} {word}\n")
                    out_lines.append(f"{meaning}\n")
                    if others and others.lower() != 'none':
                        out_lines.append(f"其他拼写: {others}\n")
                    out_lines.append('\n')
            # 跳过表头和分隔线
            elif line.strip().startswith('| ---'):
                continue

        out_name = f"{prefix}{part_num}_simple.md"
        with open(out_name, 'w', encoding='utf-8') as f_out:
            f_out.writelines(out_lines)
        print(f"已生成 {out_name}")

if __name__ == '__main__':
    convert_table_to_headings(12)