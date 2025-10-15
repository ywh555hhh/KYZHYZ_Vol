import json
import os

def json_to_markdown(json_file, md_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    def dict_to_md_table(d):
        keys = list(d.keys())
        header = '| ' + ' | '.join(keys) + ' |\n'
        sep = '| ' + ' | '.join(['---'] * len(keys)) + ' |\n'
        row = '| ' + ' | '.join(str(d[k]) for k in keys) + ' |\n'
        return header + sep + row

    def list_of_dicts_to_md_table(lst):
        if not lst:
            return ''
        keys = list(lst[0].keys())
        header = '| ' + ' | '.join(keys) + ' |\n'
        sep = '| ' + ' | '.join(['---'] * len(keys)) + ' |\n'
        rows = ''
        for item in lst:
            rows += '| ' + ' | '.join(str(item.get(k, '')) for k in keys) + ' |\n'
        return header + sep + rows

    def to_md(data, level=1):
        md = ''
        if isinstance(data, dict):
            for k, v in data.items():
                md += f"{'#' * level} {k}\n\n"
                md += to_md(v, level + 1)
        elif isinstance(data, list):
            if all(isinstance(i, dict) for i in data):
                md += list_of_dicts_to_md_table(data) + '\n'
            else:
                for i, v in enumerate(data, 1):
                    md += f"- {v}\n"
        else:
            md += f"{data}\n\n"
        return md

    md_content = to_md(data)
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

if __name__ == '__main__':
    json_path = 'netem_full_list.json'
    md_path = os.path.splitext(json_path)[0] + '.md'
    json_to_markdown(json_path, md_path)
    print(f'转换完成，已生成 {md_path}')
