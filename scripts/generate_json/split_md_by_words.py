import os

def split_markdown_by_words(md_file, words_per_file=500, output_prefix='netem_full_list_part'):
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    word_lines = []
    header = None
    for line in lines:
        if line.strip().startswith('|') and '|' in line:
            if header is None:
                header = line.strip()  # 表头
                continue
            if set(line.strip()) == {'|', '-', ' '}:
                continue  # 跳过分隔线
            word_lines.append(line.strip())

    # 新表头，增加熟悉度一列
    if header:
        new_header = header.rstrip('|') + ' | 熟悉度(0/1/2) |\n'
        col_count = header.count('|')
        sep = '| ' + ' | '.join(['---'] * (col_count - 1)) + ' | --- |\n'
    else:
        new_header = '| 单词 | 熟悉度(0/1/2) |\n'
        sep = '| --- | --- |\n'
        word_lines = [w.strip() for w in lines if w.strip()]

    total = len(word_lines)
    num_files = (total + words_per_file - 1) // words_per_file

    for i in range(num_files):
        part = word_lines[i*words_per_file:(i+1)*words_per_file]
        out_path = f'{output_prefix}{i+1}.md'
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(new_header)
            f.write(sep)
            for line in part:
                if '|' in line:
                    f.write(line.rstrip('|') + ' |   |\n')
                else:
                    f.write(f'| {line} |   |\n')
        print(f'已生成 {out_path}')

if __name__ == '__main__':
    split_markdown_by_words('netem_full_list.md')